# -*- coding: utf-8 -*-
from django_mysql.models import Model, JSONField
from django.db import models

class Bairro(models.Model):
    nome = models.CharField(
        max_length=300
    )
    aisp = models.IntegerField()
    risp = models.IntegerField()

    def __str__(self):
        return self.nome

class BairrosZonas(models.Model):
    nome = models.CharField(
        max_length=300
    )
    zona = models.IntegerField()

    def __str__(self):
        return "%s - %s" % (self.nome, self.zona)
    
class OcorrenciasMesData(Model):
    cisp = models.IntegerField()
    mes = models.IntegerField()
    ano = models.IntegerField()
    aisp = models.IntegerField()
    risp = models.IntegerField()
    regiao = models.CharField(
        max_length=300
    )
    municipio = models.CharField(
        max_length=400
    )
    mcirc = models.IntegerField()
    ocorrencias = JSONField()

    def __str__(self):
        return "%s/%s - %s" % (self.mes, self.ano, self.municipio)

    def to_json(self):
        data = {
            "id": self.id,
            "cisp": self.cisp,
            "mes": self.mes,
            "ano": self.ano,
            "aisp": self.aisp,
            "risp": self.risp,
            "regiao": self.regiao,
            "municipio": self.municipio,
            "mcirc": self.mcirc,
            "ocorrencias": self.ocorrencias
        }

        return data

class VotacaoBairro(models.Model):
    ano = models.IntegerField()
    zona = models.IntegerField()
    bairro = models.CharField(
        max_length=300
    )
    nome_candidato = models.CharField(
        max_length=300
    )
    partido = models.CharField(
        max_length=300
    )
    qt_votos = models.IntegerField()
    situacao = models.CharField(
        max_length=300
    )
    total_votos = models.IntegerField()
    proporcao = models.FloatField()

    def __str__(self):
        return "%s - %s" % (self.nome_candidato, self.bairro)

    def to_json_simple(self):
        data = {
            "qt_votos": self.qt_votos,
            "total_votos": self.total_votos,
            "proporcao": self.proporcao 
        }

        return data

class VotacaoMunZona(models.Model):
    ano = models.IntegerField()
    eleicao = models.CharField(
        max_length=300
    )
    uf = models.CharField(
        max_length=300
    )
    ue = models.CharField(
        max_length=300
    )
    municipio = models.CharField(
        max_length=300
    )
    zona = models.IntegerField()
    cargo = models.CharField(
        max_length=300
    )
    nome_candidato = models.CharField(
        max_length=600
    )
    nome_urna_candidato = models.CharField(
        max_length=300
    )
    situacao = models.CharField(
        max_length=300
    )
    sigla_partido = models.CharField(
        max_length=300
    )
    nome_partido = models.CharField(
        max_length=300
    )
    votos = models.IntegerField()

    def to_json_simple(self):
        data = {
            "nome_urna_candidato": self.nome_urna_candidato,
            "cargo": self.cargo,
            "sigla_partido": self.sigla_partido,
            "votos": self.votos
        }

        return data

class ZonasEleitorais(Model):
    num = models.IntegerField()
    municipio = models.CharField(
        max_length=300
    )
    bairro = models.CharField(
        max_length=300,
        null=True
    )

    def __str__(self):
        return "%s - %s" % (self.bairro, self.num)

class PoliciaDpsAreas(models.Model):
    nome = models.CharField(
        max_length=300
    )
    batalhao = models.CharField(
        max_length=300
    )
    aisp = models.CharField(
        max_length=300
    )
    risp = models.CharField(
        max_length=300
    )
    municipio = models.CharField(
        max_length=300
    )

    def __str__(self):
        return self.nome

    def to_json(self):
        data = {
            "id": self.id,
            "nome": self.nome,
            "batalhao": self.batalhao,
            "aisp": self.aisp,
            "risp": self.risp
        }
        return data