# -*- coding: utf-8 -*-
from datetime import datetime
import csv
from data.models import OcorrenciasMesData, VotacaoMunZona, ZonasEleitorais, PoliciaDpsAreas, VotacaoBairro, BairrosZonas

meta = ['CISP', 'mes', 'vano', 'mes_ano', 'AISP', 'RISP', 'munic', 'mcirc', 'Regiao']
def populate_ocorrenciasmesdata(filepath=None, start_year=None):
    if not filepath:
        filepath = "data/csv/BaseDPEvolucaoMensalCisp.csv"
    
    if not start_year:
        start_year = datetime.now().year
    
    with open(filepath, encoding="ISO-8859-1") as file:
        csv_reader =  csv.reader(file, delimiter=";")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                header = row
                line_count += 1
            else:
                if "Rio de Janeiro" in row[header.index("munic")]:
                    if int(row[header.index("vano")]) >= int(start_year):
                        query = OcorrenciasMesData.objects.all().filter(
                            mes=row[header.index("mes")],
                            ano__gte=int(row[header.index("vano")]),
                            cisp=row[header.index("CISP")],
                            risp=row[header.index("RISP")],
                            aisp=row[header.index("AISP")]
                        )

                        if len(query) == 0:
                            mesdata_obj = OcorrenciasMesData(
                                cisp=row[header.index("CISP")],
                                mes=row[header.index("mes")],
                                ano=row[header.index("vano")],
                                aisp=row[header.index("AISP")],
                                risp=row[header.index("RISP")],
                                regiao=row[header.index("Regiao")],
                                municipio=row[header.index("munic")],
                                mcirc=row[header.index("mcirc")],
                            )

                            ocorrencias = {}
                            item_count = 0
                            for item in row:
                                if not header[item_count] in meta:
                                    ocorrencias[header[item_count]] = item
                                item_count += 1
                            
                            mesdata_obj.ocorrencias = ocorrencias
                            mesdata_obj.save()
                            print(">>>> Salvando %s/%s - %s" % (mesdata_obj.mes, mesdata_obj.ano, mesdata_obj.municipio))
                        else:
                            print(">>>> Já salvo %s/%s - %s" % (query[0].mes, query[0].ano, query[0].municipio))
                



def populate_votacao_municipio_zona(file_path=None):
    if not file_path:
        file_path = "data/csv/votacao_candidato_munzona_2018_RJ.csv"
    
    with open(file_path, encoding="ISO-8859-1") as file:
        csv_reader = csv.reader(file, delimiter=";")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                header = row
                line_count += 1
            else:
                if row[header.index("NM_MUNICIPIO")] == "RIO DE JANEIRO" and row[header.index("DS_SIT_TOT_TURNO")] == "ELEITO POR QP" or row[header.index("DS_SIT_TOT_TURNO")] == "ELEITO POR MÉDIA":
                    line_count += 1
                    query = VotacaoMunZona.objects.all().filter(
                        ano=row[header.index("ANO_ELEICAO")],
                        municipio=row[header.index("NM_MUNICIPIO")],
                        zona=row[header.index("NR_ZONA")],
                        nome_candidato=row[header.index("NM_CANDIDATO")]
                    )
                    if len(query) == 0:
                        votacao_obj = VotacaoMunZona(
                            ano=row[header.index("ANO_ELEICAO")],
                            eleicao=row[header.index("DS_ELEICAO")],
                            uf=row[header.index("SG_UF")],
                            ue=row[header.index("NM_UE")],
                            municipio=row[header.index("NM_MUNICIPIO")],
                            zona=row[header.index("NR_ZONA")],
                            cargo=row[header.index("DS_CARGO")],
                            nome_candidato=row[header.index("NM_CANDIDATO")],
                            nome_urna_candidato=row[header.index("NM_URNA_CANDIDATO")],
                            situacao=row[header.index("DS_SIT_TOT_TURNO")],
                            sigla_partido=row[header.index("SG_PARTIDO")],
                            nome_partido=row[header.index("NM_PARTIDO")],
                            votos=row[header.index("QT_VOTOS_NOMINAIS")]
                        )

                        votacao_obj.save()
                        print(">>>> Salvando %s - %s - %s" % (votacao_obj.nome_urna_candidato, votacao_obj.votos, votacao_obj.zona))

def populate_zonas(file_path=None):
    if not file_path:
        file_path = "data/csv/eleitoral_locais_2018.csv"
    
    with open(file_path, encoding="UTF-8") as file:
        csv_reader = csv.reader(file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                header = row
                line_count += 1
            else:
                if row[header.index("municipio")] == "RIO DE JANEIRO":
                    query = ZonasEleitorais.objects.all().filter(
                        num=row[header.index("zona_eleitoral")],
                        municipio=row[header.index("municipio")],
                        bairro=row[header.index("bairro")]
                    )
                    if len(query) == 0:
                        zona = ZonasEleitorais(
                            num=row[header.index("zona_eleitoral")],
                            municipio=row[header.index("municipio")],
                            bairro=row[header.index("bairro")]
                        )
                        zona.save()
                        print(">>>> Salvando Zona %s" % zona.num)

def populate_dps_areas(file_path=None):
    if not file_path:
        file_path = "data/csv/policia_dps_areas.csv"
    
    with open(file_path, encoding="utf8") as file:
        csv_reader = csv.reader(file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                header = row
                line_count += 1
            else:
                if row[header.index("Município_da_DP")] == "Rio de Janeiro":
                    area = PoliciaDpsAreas(
                        nome=row[header.index("Nome_da_Delegacia")],
                        batalhao=row[header.index("Batalhão")],
                        aisp=row[header.index("AISP_2017")],
                        risp=row[header.index("RISP")],
                        municipio=row[header.index("Município_da_DP")]
                    )
                    area.save()
                    print(">>>> Salvando ...")

def populate_bairros_zonas(file_path=None):
    if not file_path:
        file_path = "data/csv/bairros_list.csv"
    
    with open(file_path, encoding="utf8") as file:
        csv_reader = csv.reader(file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                header = row
                line_count += 1
            else:
                bairros = row[header.index("bairros")].split(", ")
                for b in bairros:
                    query = BairrosZonas.objects.all().filter(
                        nome=b
                    )
                    if len(query) == 0:
                        bz = BairrosZonas(
                            nome=b,
                            zona=int(row[0])
                        )
                        bz.save()
                        print(">>>> Salvo %s" % bz.__str__())


def populate_votacao_bairros(file_path=None):
    if not file_path:
        file_path = "data/csv/votacoes_bairros.csv"
    
    with open(file_path, encoding="utf8") as file:
        csv_reader = csv.reader(file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                header = row
                line_count += 1
            else:
                query = VotacaoBairro.objects.all().filter(
                    ano=int(row[header.index("ano")]),
                    nome_candidato=row[header.index("nome_candidato")],
                    zona=row[header.index("zona")]
                )
                if len(query) == 0:
                    obj = VotacaoBairro(
                        ano=int(row[header.index("ano")]),
                        nome_candidato=row[header.index("nome_candidato")],
                        zona=row[header.index("zona")],
                        bairro=row[header.index("bairro")],
                        partido=row[header.index("partido")],
                        qt_votos=int(row[header.index("qt_votos")]),
                        situacao=row[header.index("situacao")],
                        total_votos=int(row[header.index("total_votos")]),
                        proporcao=float(row[header.index("proporcao")])
                    )
                    obj.save()
                    print(">>>> Salvando %s..." % obj.__str__())


