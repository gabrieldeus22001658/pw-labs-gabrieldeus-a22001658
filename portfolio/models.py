from django.db import models


# Create your models here.

#TODO Lab 10
#Esboço das Classes para a base de dados do lab10

class Cadeira(models.Model):
    nome = models.CharField(max_length=64)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    ano_letivo = models.CharField(max_length=10)
    topicos = models.CharField(max_length=64)
    ranking = models.IntegerField()
    pagina = models.CharField(max_length=64)
    professores = None  # One-To-Many
    projetos = None  # One-To-Many


class Pessoa(models.Model):
    nome = models.CharField(max_length=64)
    linkLusofona = models.CharField(max_length=64)
    linkLinkedin = models.CharField(max_length=64)
    linkPortfolio = models.CharField(max_length=64)


class Projeto(models.Model):
    titulo = models.CharField(max_length=64)
    descrição = models.CharField(max_length=500)
    imagem = None  # One-To-One
    ano_realizado = models.IntegerField()
    cadeira = None  # One-To-One
    participantes = None  # One-To-Many
    github = models.CharField(max_length=64)
    linkYt = models.CharField(max_length=64)
    tecnologias = models.CharField(max_length=64)
    competencias = None  # One-To-Many
    projeto = models.CharField(max_length=64)
