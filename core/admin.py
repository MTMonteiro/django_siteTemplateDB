from django.contrib import admin

from .models import Cargo, Servico, Funcionario, Features


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'modificado', 'ativo')


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Features)
class FeaturesAdin(admin.ModelAdmin):
    list_display = ('recurso', 'descricao', 'posicao', 'icone', 'ativo', 'modificado')


