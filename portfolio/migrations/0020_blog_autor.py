# Generated by Django 4.0.6 on 2022-07-27 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_remove_blog_autor_alter_blog_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='autor',
            field=models.CharField(default='Anônimo', max_length=30, null=True),
        ),
    ]