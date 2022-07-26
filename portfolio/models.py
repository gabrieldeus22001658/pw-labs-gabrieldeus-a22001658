from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Pessoa(models.Model):
    nome = models.CharField(max_length=64)
    linkLusofona = models.URLField(blank=True, null=True, max_length=200)
    linkLinkedin = models.URLField(blank=True, null=True, max_length=200)

    def __str__(self):
        return f"{self.nome}"


class Cadeira(models.Model):
    nome = models.CharField(max_length=64)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    ects = models.IntegerField()
    ano_letivo = models.CharField(max_length=10)
    topicos = models.CharField(max_length=300)
    ranking = models.IntegerField()
    pagina = models.URLField(max_length=200)
    professores = models.ForeignKey(Pessoa, null=False, on_delete=models.CASCADE, related_name='prof')
    professorAuxiliar = models.ForeignKey(Pessoa, blank=True, null=True, on_delete=models.CASCADE, related_name='prof2')

    def __str__(self):
        return f"{self.nome}"


class Competencia(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    nivel = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome}"


class Projeto(models.Model):
    titulo = models.CharField(max_length=64)
    descricao = models.CharField(max_length=500)
    imagem = models.ImageField(null=True, blank=True, upload_to="imagem/")
    ano_realizado = models.IntegerField()
    participante1 = models.ForeignKey(Pessoa, null=True, on_delete=models.CASCADE, related_name="p1")
    participante2 = models.ForeignKey(Pessoa, blank=True, null=True, on_delete=models.CASCADE, related_name="p2")
    github = models.URLField(blank=True, null=True, max_length=200)
    linkYt = models.URLField(blank=True, null=True, max_length=200)
    tecnologias = models.CharField(max_length=100)
    competencias = models.ForeignKey(Competencia, on_delete=models.CASCADE)
    cadeira = models.ForeignKey(Cadeira, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo}"


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
