# -*- coding: utf-8 -*-
from django_mysql.models import Model, JSONField
from django.db import models

# Relação de bairros e AISP e RISP
class Bairro(models.Model):
    nome = models.CharField(
        max_length=300
    )
    aisp = models.IntegerField()
    risp = models.IntegerField()

    def __str__(self):
        return self.nome

# Ocorrências por mes    
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

# Votação por municipio e zona eleitoral
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

# Relaçao de bairros e zonas eleitorais
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

class RendaDomicilios(Model):
    municipio = models.CharField(
        max_length=300
    )
    distrito = models.CharField(
        max_length=300
    )
    bairro = models.CharField(
        max_length=300
    )
    meio_salario = models.FloatField()
    meio_2salarios = models.FloatField()
    de_2salarios_5salarios = models.FloatField()
    de_5salarios_10salarios = models.FloatField()
    acima_10salarios = models.FloatField()
    sem_rendimentos = models.FloatField()
    total_domicilios = models.IntegerField()

    def __str__(self):
        return "%s -%s" % (self.municipio, self.bairro)

    def to_json(self):
        data = {
            "id": self.id,
            "municipio": self.municipio,
            "bairro": self.bairro,
            "meio_salario": self.meio_salario,
            "meio_2salarios": self.meio_2salarios,
            "de_2salarios_5salarios": self.de_2salarios_5salarios,
            "de_5salarios_10salarios": self.de_5salarios_10salarios,
            "acima_10salarios": self.acima_10salarios,
            "sem_rendimentos": self.sem_rendimentos,
            "total_domicilios": self.total_domicilios
        }
    
        return data
