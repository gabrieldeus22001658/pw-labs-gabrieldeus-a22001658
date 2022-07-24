# Generated by Django 4.0.4 on 2022-07-22 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_pontuacaoquizz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competencia', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('linkLusofona', models.URLField()),
                ('linkLinkedin', models.URLField()),
                ('linkPortfolio', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=64)),
                ('descricao', models.CharField(max_length=500)),
                ('imagem', models.ImageField(upload_to='')),
                ('ano_realizado', models.IntegerField()),
                ('github', models.URLField()),
                ('linkYt', models.URLField()),
                ('tecnologias', models.CharField(max_length=64)),
                ('projeto', models.CharField(max_length=64)),
                ('competencias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.competencia')),
                ('participantes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('ects', models.IntegerField()),
                ('ano_letivo', models.CharField(max_length=10)),
                ('topicos', models.CharField(max_length=64)),
                ('ranking', models.IntegerField()),
                ('pagina', models.URLField()),
                ('professores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.pessoa')),
                ('projetos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.projeto')),
            ],
        ),
    ]
