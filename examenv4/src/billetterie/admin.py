from django.contrib import admin
from .models import Offre, Achat, Utilisateur


class OffreAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'count_achats')
    search_fields = ('nom',)

admin.site.register(Offre, OffreAdmin)
admin.site.register(Achat)
admin.site.register(Utilisateur)
