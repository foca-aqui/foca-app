# coding: utf-8 -*-
from datetime import datetime
from django.db.models.query import QuerySet
from api.mixins import APIViewMixin

from parlamentares.models import Parlamentar
from data.models import Bairro, OcorrenciasMesData, ZonasEleitorais, VotacaoMunZona, RendaDomicilios
from api.constants import CRIMES_VIOLENTOS, CRIMES_DICT

class ParlamentaresView(APIViewMixin):
    get_services = ("get_parlamentares_by_bairros", "get_parlamentar_details")

    def _get_parlamentar_details(self, data):
        response = {}
        nome = data.get("nome")
        if nome:
            query = Parlamentar.objects.all().filter(
                nome=nome.upper()
            )
            if len(query) > 0:
                response = query[0].to_json()

        return response

    def _get_parlamentares_by_bairros(self, data):
        response = {}

        bairros_str = data.get("bairros")
        if bairros_str:
            bairros = bairros_str.split(",")
            zonas = []

            for b in bairros:
                b_zonas = ZonasEleitorais.objects.all().filter(
                    bairro=b.upper()
                )
                for z in b_zonas:
                    zonas.append(z.num)
            
            votacao_federal = {}
            votacao_estadual = {}
            for z in zonas:
                vf = VotacaoMunZona.objects.all().filter(
                    zona=z,
                    cargo="Deputado Federal"
                ).order_by("-votos")[:5]
                for item in vf:
                    if item.nome_urna_candidato in votacao_federal:
                        votacao_federal[item.nome_urna_candidato]["votos"] += item.votos
                    else:
                        votacao_federal[item.nome_urna_candidato] = item.to_json_simple()
                
                ve = VotacaoMunZona.objects.all().filter(
                    zona=z,
                    cargo="Deputado Estadual"
                ).order_by("-votos")[:5]
                for item in ve:
                    if item.nome_urna_candidato in votacao_estadual:
                        votacao_estadual[item.nome_urna_candidato]["votos"] += item.votos
                    else:
                        votacao_estadual[item.nome_urna_candidato] = item.to_json_simple()

            response["federais"] = votacao_federal           
            response["estaduais"] = votacao_estadual
        
        return response

class RendaDomiciliosView(APIViewMixin):
    get_services = ("get_by_bairro", )

    def _get_by_bairro(self, data):
        response = []

        bairro = data.get("bairro")
        if bairro:
            query = RendaDomicilios.objects.all().filter(
                municipio="RIO DE JANEIRO",
                bairro__contains=bairro
            )
            for q in query:
                response.append(q.to_json())
        
        return response


class OcorrenciasView(APIViewMixin):
    get_services = ("get_ocorrencias", "get_top_ocorrencias", "get_ocorrencias_by_bairro", "get_top_ocorrencias_by_bairro")

    def _get_ocorrencias_by_bairro(self, data):
        bairro = data.get("bairro")
        mes = data.get("mes")
        aisp = None
        for b in Bairro.objects.all():
            if bairro.lower() in b.nome.lower():
                aisp = b.aisp
        
        if aisp:
            return self._get_ocorrencias(
                data={"aisp": aisp, "mes": mes}
            )
        else:
            return {"status": "informe um bairro válido"}

    def _get_top_ocorrencias_by_bairro(self, data):
        bairro = data.get("bairro")
        aisp = None
        for b in Bairro.objects.all():
            if bairro.lower() in b.nome.lower():
                aisp = b.aisp
        
        if aisp:
            return self._get_top_ocorrencias(
                data={ "aisp": aisp }
            )
        else:
            return {"status": "informe um bairro válido"}

    def _get_ocorrencias(self, data):
        response = {}

        aisp = data.get("aisp")
        risp = data.get("risp")
        ano = data.get("ano")
        mes = data.get("mes")
        if not ano:
            ano = datetime.now().year
        if not mes:
            mes = OcorrenciasMesData.objects.order_by('-pk')[0].mes
        
        if aisp:
            ocorrencias = OcorrenciasMesData.objects.all().filter(
                ano=int(ano),
                mes=mes,
                aisp=aisp
            )
        elif risp:
            ocorrencias = OcorrenciasMesData.objects.all().filter(
                ano=int(ano),
                mes=mes,
                risp=risp
            )
        else:
            ocorrencias = OcorrenciasMesData.objects.all().filter(
                ano=int(ano),
                mes=mes,
            )

        indice = {
            "crimes_violentos": 0,
            "roubos_furtos": 0
        }
        fields = ["apf", "cmp", "cmba", "fase", "aaapai"]
        for o in ocorrencias:
            for key, value in o.ocorrencias.items():
                if not key in fields:
                    if key in CRIMES_VIOLENTOS:
                        indice["crimes_violentos"] += int(value or 0)
            indice["roubos_furtos"] += int(o.ocorrencias["total_roubos"]) + int(o.ocorrencias["total_furtos"])
        
        response["top_ocorrencias"] = [{k: indice[k]} for k in sorted(indice, key=indice.get, reverse=True)]

        return response
    
    def _get_top_ocorrencias(self, data):
        response = {}

        aisp = data.get("aisp")
        risp = data.get("risp")
        ano = data.get("ano")
        if not ano:
            ano = datetime.now().year
        
        if aisp:
            ocorrencias = OcorrenciasMesData.objects.all().filter(
                ano=int(ano),
                aisp=aisp
            )
            bairros = []
            for b in Bairro.objects.all().filter(aisp=aisp):
                if not b.nome in bairros:
                    bairros.append(b.nome)
            response["bairros"] = bairros
            
        elif risp:
            ocorrencias = OcorrenciasMesData.objects.all().filter(
                ano=int(ano),
                risp=risp
            )
            response["bairros"] = [b.nome for b in Bairro.objects.all().filter(risp=risp)]

        indice = {}
        fields = ["apf", "cmp", "cmba", "fase", "aaapai", "registro_ocorrencias", "indicador_roubo_rua", "outros_furtos"]
        for o in ocorrencias:
            for key, value in o.ocorrencias.items():
                if not key in fields and not "furto_" in key and not "roubo_" in key:
                    if len(key) > 1 and key in indice:
                        indice[key] += int(value or 0)
                    else:
                        indice[key] = int(value or 0)
        
        response["top_ocorrencias"] = [{CRIMES_DICT[k]: indice[k]} for k in sorted(indice, key=indice.get, reverse=True) if k in CRIMES_DICT]
    
        return response

