from django.contrib import admin

from .models import Blog, PontuacaoQuizz, Projeto, Pessoa, Competencia, Cadeira, Noticia, TFC

admin.site.register(Cadeira)
admin.site.register(Blog)
admin.site.register(PontuacaoQuizz)
admin.site.register(Projeto)
admin.site.register(Pessoa)
admin.site.register(Competencia)
admin.site.register(Noticia)
admin.site.register(TFC)
