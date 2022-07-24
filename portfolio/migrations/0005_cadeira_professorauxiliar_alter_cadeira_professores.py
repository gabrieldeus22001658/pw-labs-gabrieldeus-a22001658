# Generated by Django 4.0.4 on 2022-07-23 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_remove_pessoa_linkportfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadeira',
            name='professorAuxiliar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prof2', to='portfolio.pessoa'),
        ),
        migrations.AlterField(
            model_name='cadeira',
            name='professores',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prof', to='portfolio.pessoa'),
        ),
    ]
