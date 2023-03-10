from django.contrib import admin

from .models import Clientes


class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'cpf')
    list_display_links = ('id', 'nome_completo', 'cpf')


admin.site.register(Clientes, ClientesAdmin)

