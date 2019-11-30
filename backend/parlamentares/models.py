# -*- coding: utf-8 -*-
from django.db import models

DEPUTADO_TYPE = (
    ("Deputado Estadual", "Deputado Estadual"),
    ("Deputado Federal", "Deputado Federal"),
)

class Parlamentar(models.Model):
    nome = models.CharField(
        max_length=300
    )
    deputado = models.CharField(
        max_length=300,
        choices=DEPUTADO_TYPE
    )
    img_url = models.CharField(
        max_length=300
    )
    telefone = models.CharField(
        max_length=300
    )
    email = models.CharField(
        max_length=300
    )

    def to_json(self):
        data = {
            "nome": self.nome,
            "deputado": self.deputado,
            "img_url": self.img_url,
            "telefone": self.telefone,
            "email": self.email
        }

        return data
        
    def __str__(self):
        return "%s - %s" % (self.nome, self.deputado) 

class ParlamentaresVotacao(models.Model):
    ano = models.IntegerField()
    municipio = models.CharField(
        max_length=300
    )
    zona = models.IntegerField()
    cargo = models.CharField(
        max_length=300
    )
    nome = models.CharField(
        max_length=300
    )
    nome_urna = models.CharField(
        max_length=300
    )
    sg_partido = models.CharField(
        max_length=300
    )
    partido = models.CharField(
        max_length=300
    )
    votos = models.IntegerField()
    proporcao = models.FloatField()
    porcentagem = models.FloatField()
    situacao = models.CharField(
        max_length=300
    )

    def to_json(self):
        data = {
            "id": self.id,
            "ano": self.ano,
            "municipio": self.municipio,
            "zona": self.zona,
            "nome": self.nome,
            "nome_urna": self.nome_urna,
            "sg_partido": self.sg_partido,
            "partido": self.partido,
            "votos": self.votos,
            "proporcao": self.proporcao,
            "porcentagem": self.porcentagem
        }

        return data

    def __str__(self):
        return "%s - %s > %s" % (self.nome_urna, self.cargo, self.ano)

