from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

# class Cadeira(models.Model):
#    nome = models.CharField(max_length=64)
#    ano = models.IntegerField()
#   semestre = models.IntegerField()
#   ects = models.IntegerField()
#   ano_letivo = models.CharField(max_length=10)
#   topicos = models.CharField(max_length=64)
#  ranking = models.IntegerField()
#  pagina = models.URLField(max_length=200)
#  professores = None  # One-To-Many
#  projetos = None  # One-To-Many


# class Pessoa(models.Model):
#  nome = models.CharField(max_length=64)
#  linkLusofona = models.URLField(max_length=200)
#  linkLinkedin = models.URLField(max_length=200)
#  linkPortfolio = models.URLField(max_length=200)


# class Projeto(models.Model):
# titulo = models.CharField(max_length=64)
# descricao = models.CharField(max_length=500)
# imagem = None
#  ano_realizado = models.IntegerField()
#  cadeira = None  # One-To-One
# participantes = None  # One-To-Many
#  github = models.URLField(max_length=200)
# linkYt = models.URLField(max_length=200)
# tecnologias = models.CharField(max_length=64)
#  competencias = None  # One-To-Many
#  projeto = models.CharField(max_length=64)


class Blog(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self):
        return str(self.titulo) + ' | ' + str(self.autor)

    def get_absolute_url(self):
        return reverse('portfolio:blog-details', args=(str(self.pk)))


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=30)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)
