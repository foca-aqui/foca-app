from django.contrib import admin
from data.models import Bairro, OcorrenciasMesData, ZonasEleitorais, VotacaoMunZona, PoliciaDpsAreas, VotacaoBairro, BairrosZonas

admin.site.register(Bairro)
class OcorrenciasAdmin(admin.ModelAdmin):
    list_filter = ("ano", "aisp", "risp", "cisp")
admin.site.register(OcorrenciasMesData, OcorrenciasAdmin)

class VotacaoBairroAdmin(admin.ModelAdmin):
    list_filter = ("bairro", "partido")
    search_fields = ("nome_candidato", "bairro")
admin.site.register(VotacaoBairro, VotacaoBairroAdmin)

class BairrosZonasAdmin(admin.ModelAdmin):
    search_fields = ("nome", )
admin.site.register(BairrosZonas, BairrosZonasAdmin)

admin.site.register(ZonasEleitorais)
admin.site.register(VotacaoMunZona)
admin.site.register(PoliciaDpsAreas)