import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog, PontuacaoQuizz
from .forms import BlogForm, EditBlogForm
from django.urls import reverse_lazy


def index_view(request):
    return render(request, 'portfolio/hero.html')


def home_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }
    return render(request, 'portfolio/home.html', context)


def comp_page_view(request):
    return render(request, 'portfolio/competencias.html')


def formac_page_view(request):
    return render(request, 'portfolio/formação.html')


def proj_page_view(request):
    return render(request, 'portfolio/projetos.html')


def apr_page_view(request):
    return render(request, 'portfolio/apresentação.html')


def lic_page_view(request):
    return render(request, 'portfolio/licenciatura.html')


class HomeView(ListView):
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
    # fields = ['titulo', 'descricao']


class DeleteBlog(DeleteView):
    model = Blog
    template_name = 'portfolio/delete_blog.html'
    success_url = reverse_lazy('portfolio:home')


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
