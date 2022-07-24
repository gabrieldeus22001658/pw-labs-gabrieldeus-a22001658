from django.contrib import admin

from .models import Blog, PontuacaoQuizz, Projeto, Pessoa, Competencia, Cadeira

admin.site.register(Cadeira)
admin.site.register(Blog)
admin.site.register(PontuacaoQuizz)
admin.site.register(Projeto)
admin.site.register(Pessoa)
admin.site.register(Competencia)
