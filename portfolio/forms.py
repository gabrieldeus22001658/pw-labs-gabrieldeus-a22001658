from django import forms
from django.forms import ModelForm
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva um título...'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
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
            # 'autor': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva aqui...'}),
        }

        labels = {
            'titulo': 'Título',
        }
