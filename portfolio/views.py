from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog, PontuacaoQuizz, Pessoa, Projeto, Competencia, Cadeira, TFC, Noticia
from .forms import BlogForm, EditBlogForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages


def resolution_path(instance, filename):
    return f'users/{instance.id}/'


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('portfolio:home')
        else:
            messages.success(request, "Login Inválido, tente outra vez")
            return redirect('portfolio:login')
    else:
        return render(request, 'portfolio/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('portfolio:home')


def index_view(request):
    return render(request, 'portfolio/hero.html')


class BlogView(ListView):
    model = Blog
    template_name = 'portfolio/home.html'


class BlogDetail(DetailView):
    model = Blog
    template_name = 'portfolio/blog_details.html'


class AddBlog(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'portfolio/add_blog.html'


class UpdateBlog(UpdateView):
    model = Blog
    form_class = EditBlogForm
    template_name = 'portfolio/edit_blog.html'


class DeleteBlog(DeleteView):
    model = Blog
    template_name = 'portfolio/delete_blog.html'
    success_url = reverse_lazy('portfolio:blog')


def pontuacao_quizz(request):
    score = 0
    if request.POST["back"] == "Javascript":
        score += 1
    if request.POST["CSS"] == "Cascading Style Sheets":
        score += 1
    if request.POST["HTML"] == "Hypertext Markup Language":
        score += 1
    if request.POST["Spotify"] == "Django":
        score += 1
    if request.POST["Django"] == "Python":
        score += 1
    return score


def quizz_view(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        obj = PontuacaoQuizz(nome=n, score=p)
        data = PontuacaoQuizz.objects.all()
        obj.save()
        context = {
            'score': p,
            'data': data,
        }
        return render(request, 'portfolio/quizz.html', context)
    return render(request, 'portfolio/quizz.html')


def desenha_grafico_resultados(request):
    nomes = []
    scores = []
    for r in PontuacaoQuizz.objects.all():
        nomes.append(r.nome)
        scores.append(r.score)
    nomes.reverse()
    scores.reverse()


def lista_cadeiras(request):
    context = {
        'cadeiras': Cadeira.objects.all(),
        'range': range(1, 6)
    }
    return render(request, 'portfolio/licenciatura.html', context)


def lista_projetos(request):
    context = {
        'projetos': Projeto.objects.all(),
    }
    return render(request, 'portfolio/projetos.html', context)


def apresentacao_view(request):
    context = {
        'competencias': Competencia.objects.all(),
    }
    return render(request, 'portfolio/apresentação.html', context)


def lista_tfcs(request):
    context = {
        'tfcs': TFC.objects.all(),
    }
    return render(request, 'portfolio/tfcs.html', context)


def lista_noticias(request):
    context = {
        'noticias': Noticia.objects.all(),
    }
    return render(request, 'portfolio/noticias.html', context)
