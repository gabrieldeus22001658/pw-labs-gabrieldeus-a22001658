# Generated by Django 4.0.4 on 2022-07-25 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_alter_pessoa_linklinkedin_alter_pessoa_linklusofona'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='linkYt',
            field=models.URLField(blank=True, null=True),
        ),
    ]