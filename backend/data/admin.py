from django.contrib import admin
from data.models import Bairro, OcorrenciasMesData, ZonasEleitorais, VotacaoMunZona, RendaDomicilios

admin.site.register(Bairro)
class OcorrenciasAdmin(admin.ModelAdmin):
    list_filter = ("ano", "aisp", "risp", "cisp")
admin.site.register(OcorrenciasMesData, OcorrenciasAdmin)

admin.site.register(RendaDomicilios)
admin.site.register(ZonasEleitorais)
admin.site.register(VotacaoMunZona)