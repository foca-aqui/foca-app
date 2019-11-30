# -*- coding: utf-8 -*-
import json, csv
from parlamentares.models import Parlamentar, ParlamentaresVotacao

def populate_estaduais(file_path=None):
    if not file_path:
        file_path = "parlamentares/data/estaduais.json"
    
    with open(file_path) as file:
        data = json.load(file)
        for p in data:
            obj = Parlamentar(
                nome=p["nome"],
                deputado="Deputado Estadual",
                img_url=p["img_url"],
                telefone=p["telefone"],
                email=p["email"]
            )
            obj.save()

            print(">>>> Salvando %s" % obj.__str__())

def populate_cmrj(file_path=None):
    if not file_path:
        file_path = "parlamentares/data/cmrj.json"
    
    with open(file_path) as file:
        data = json.load(file)
        for p in data:
            obj = Parlamentar(
                nome=p["nome"],
                deputado="Vereador",
                img_url=p["img_url"],
                telefone=p["telefone"]
            )
            if "email" in p:
                obj.email = p["email"]
            obj.save()

            print(">>>> Salvando %s" % obj.__str__())

def populate_federais(file_path=None):
    if not file_path:
        file_path = "parlamentares/data/federais.csv"
    
    with open(file_path, encoding="ISO-8859-1") as file:
        csv_reader = csv.reader(file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                header = row
                line_count += 1
            else:
                query = Parlamentar.objects.all().filter(
                    nome=row[0]
                )
                if len(query) == 0:
                    obj = Parlamentar(
                        nome=row[0],
                        deputado="Deputado Federal",
                        telefone=row[9],
                        email=row[13]
                    )
                    obj.save()
                    print(">>>> Salvando %s" % obj.__str__())

def populate_votacao(file_path=None):
    if file_path:
        with open(file_path, encoding="utf-8") as file:
            csv_reader = csv.reader(file, delimiter=",")
            line_count = 0
            for row in csv_reader:
                if line_count > 0 and row[4] == "6" or row[4] == "7" or row[4] == "13":
                    #Verifica se o dado já existe
                    query = ParlamentaresVotacao.objects.all().filter(
                        ano=row[0],
                        nome=row[7],
                        zona=row[3]
                    )
                    if len(query) == 0:
                        obj = ParlamentaresVotacao(
                            ano=row[0],
                            municipio=row[2],
                            zona=row[3],
                            cargo=row[5],
                            nome=row[7],
                            nome_urna=row[8],
                            sg_partido=row[10],
                            partido=row[11],
                            votos=row[15],
                            situacao=row[14],
                            proporcao=row[16],
                            porcentagem=row[17]
                        )
                        obj.save()

                        print(">>> Salvo %s" % obj.__str__())
