# -*- coding: utf-8 -*-
from datetime import datetime
import csv
from data.models import OcorrenciasMesData, VotacaoMunZona, ZonasEleitorais, RendaDomicilios

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

def perc(total, parte):
    return parte/total * 100

def populate_renda_domicilios(file_path=None):
    if not file_path: 
        file_path = "data/csv/censo2010_renda_domicilios.csv"
    
    with open(file_path, encoding="utf-8") as file:
        csv_reader = csv.reader(file, delimiter=",")
        line_count = 0
        data = {}
        for row in csv_reader:
            if line_count == 0:
                header = row
                line_count += 1
            else:
                #import pdb; pdb.set_trace()
                if row[header.index("Municipio")] == "RIO DE JANEIRO":
                    if not row[header.index("Bairro")] in data:
                        data[row[header.index("Bairro")]] = {
                            "distrito": row[header.index("Distrito")],
                            "até_meio_salario": int(row[header.index("até_meio_salario")] if row[header.index("até_meio_salario")] else 0),
                            "acima_de_meio_salario_até_2salarios": int(row[header.index("acima_de_meio_salario_até_2salarios")] if row[header.index("acima_de_meio_salario_até_2salarios")] else 0),
                            "acima_de_2salarios_até_5salarios": int(row[header.index("acima_de_2salarios_até_5salarios")] if row[header.index("acima_de_2salarios_até_5salarios")] else 0),
                            "acima_de_5salarios_até_10salarios": int(row[header.index("acima_de_5salarios_até_10salarios")] if row[header.index("acima_de_5salarios_até_10salarios")] else 0),
                            "acima_10salarios": int(row[header.index("acima_10salarios")] if row[header.index("acima_10salarios")] else 0),
                            "sem_rendimentos": int(row[header.index("sem_rendimentos")] if row[header.index("sem_rendimentos")] else 0),
                            "total_domicilios": int(row[header.index("total_domicilios")] if row[header.index("total_domicilios")] else 0)
                        }
                    else:
                        data[row[header.index("Bairro")]]["até_meio_salario"] += int(row[header.index("até_meio_salario")] if row[header.index("até_meio_salario")] else 0)
                        data[row[header.index("Bairro")]]["acima_de_meio_salario_até_2salarios"] += int(row[header.index("acima_de_meio_salario_até_2salarios")] if row[header.index("acima_de_meio_salario_até_2salarios")] else 0)
                        data[row[header.index("Bairro")]]["acima_de_2salarios_até_5salarios"] += int(row[header.index("acima_de_2salarios_até_5salarios")] if row[header.index("acima_de_meio_salario_até_2salarios")] else 0)
                        data[row[header.index("Bairro")]]["acima_de_5salarios_até_10salarios"] += int(row[header.index("acima_de_5salarios_até_10salarios")] if row[header.index("acima_de_5salarios_até_10salarios")] else 0)
                        data[row[header.index("Bairro")]]["acima_10salarios"] += int(row[header.index("acima_10salarios")] if row[header.index("acima_10salarios")] else 0)
                        data[row[header.index("Bairro")]]["sem_rendimentos"] += int(row[header.index("sem_rendimentos")] if row[header.index("sem_rendimentos")] else 0)
                        data[row[header.index("Bairro")]]["total_domicilios"] += int(row[header.index("total_domicilios")] if row[header.index("total_domicilios")] else 0)
        
        for bairro in data:
            #import pdb; pdb.set_trace()
            reg = RendaDomicilios(
                municipio="RIO DE JANEIRO",
                distrito=data[bairro]["distrito"],
                bairro=bairro,
                meio_salario=perc(data[bairro]["total_domicilios"], data[bairro]["até_meio_salario"]),
                meio_2salarios=perc(data[bairro]["total_domicilios"], data[bairro]["acima_de_meio_salario_até_2salarios"]),
                de_2salarios_5salarios=perc(data[bairro]["total_domicilios"], data[bairro]["acima_de_2salarios_até_5salarios"]),
                de_5salarios_10salarios=perc(data[bairro]["total_domicilios"], data[bairro]["acima_de_5salarios_até_10salarios"]),
                acima_10salarios=perc(data[bairro]["total_domicilios"], data[bairro]["acima_10salarios"]),
                sem_rendimentos=perc(data[bairro]["total_domicilios"], data[bairro]["sem_rendimentos"]),
                total_domicilios=data[bairro]["total_domicilios"]
            )

            reg.save()
            print(">>>> Salvo dados de %s" % reg.__str__())
                    

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

