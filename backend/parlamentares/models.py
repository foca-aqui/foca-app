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

    def __str__(self):
        return "%s - %s" % (self.nome, self.deputado) 
