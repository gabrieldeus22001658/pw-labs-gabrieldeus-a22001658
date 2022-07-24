# Generated by Django 4.0.4 on 2022-07-23 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_alter_cadeira_projetos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='professorAuxiliar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prof2', to='portfolio.pessoa'),
        ),
        migrations.AlterField(
            model_name='cadeira',
            name='projetos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio.projeto'),
        ),
    ]
