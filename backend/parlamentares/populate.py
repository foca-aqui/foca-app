# -*- coding: utf-8 -*-
import json, csv
from parlamentares.models import Parlamentar

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
