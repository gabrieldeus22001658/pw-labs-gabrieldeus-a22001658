from django import forms
from django.forms import ModelForm
from .models import Blog, Pessoa, Projeto, TFC, Noticia, Competencia, Cadeira


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o seu nome...'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva um título...'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva aqui...'}),
        }

        labels = {
            'titulo': 'Título',
        }


class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('titulo', 'descricao')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva um título...'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva aqui...'}),
        }

        labels = {
            'titulo': 'Título',
        }


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'


class CadeiraForm(forms.ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'


class TFCForm(forms.ModelForm):
    class Meta:
        model = TFC
        fields = '__all__'


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
