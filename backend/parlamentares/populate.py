# -*- coding: utf-8 -*-
import json
from parlamentares.models import Parlamentar

def populate_estaduais(file_path=None):
    if not file_path:
        file_path = "parlamentares/scrapper/estaduais.json"
    
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
