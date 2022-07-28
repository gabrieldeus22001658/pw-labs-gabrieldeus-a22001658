from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog, PontuacaoQuizz, Pessoa, Projeto, Competencia, Cadeira, TFC, Noticia
from .forms import BlogForm, EditBlogForm, PessoaForm, ProjetoForm, CadeiraForm, TFCForm, NoticiaForm
from django.urls import reverse_lazy, reverse
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


def diagramas_view(request):
    return render(request, 'portfolio/diagramas.html')


def pw_view(request):
    return render(request, 'portfolio/pw.html')


def tecnologias_view(request):
    return render(request, 'portfolio/tecnologias.html')


def contacto_view(request):
    return render(request, 'portfolio/contacto.html')


@login_required
def novo_projetos_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form = ProjetoForm(request.POST or None, request.FILES)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form}
    return render(request, 'portfolio/addProjeto.html', context)


@login_required
def view_editar_projeto(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    form = ProjetoForm(request.POST or None, instance=projeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form, 'projeto_id': projeto_id}
    return render(request, 'portfolio/editProjeto.html', context)


@login_required
def view_apagar_projeto(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return HttpResponseRedirect(reverse('portfolio:projetos'))


@login_required
def nova_pessoa_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form_c = PessoaForm(request.POST or None)

    if form_c.is_valid():
        form_c.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form_c}
    return render(request, 'portfolio/addPessoa.html', context)


@login_required
def nova_cadeira_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form_c = CadeiraForm(request.POST or None)

    if form_c.is_valid():
        form_c.save()
        return HttpResponseRedirect(reverse('portfolio:apresentação'))

    context = {'form': form_c}
    return render(request, 'portfolio/addCadeira.html', context)


@login_required
def view_editar_cadeira(request, cadeira_id):
    cadeira = Cadeira.objects.get(id=cadeira_id)
    form = CadeiraForm(request.POST or None, instance=cadeira)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:apresentação'))

    context = {'form': form, 'cadeira_id': cadeira_id}
    return render(request, 'portfolio/editCadeira.html', context)


@login_required
def view_apagar_cadeira(request, cadeira_id):
    cadeira = Cadeira.objects.get(id=cadeira_id)
    cadeira.delete()
    return HttpResponseRedirect(reverse('portfolio:apresentação'))


@login_required
def novo_tfc_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form_c = TFCForm(request.POST or None, request.FILES)

    if form_c.is_valid():
        form_c.save()
        return HttpResponseRedirect(reverse('portfolio:tfcs'))

    context = {'form': form_c}
    return render(request, 'portfolio/addTFC.html', context)


@login_required
def view_editar_tfc(request, tfc_id):
    tfc = TFC.objects.get(id=tfc_id)
    form = TFCForm(request.POST or None, instance=tfc)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:tfcs'))

    context = {'form': form, 'tfc_id': tfc_id}
    return render(request, 'portfolio/editTfc.html', context)


@login_required
def view_apagar_tfc(request, tfc_id):
    tfc = TFC.objects.get(id=tfc_id)
    tfc.delete()
    return HttpResponseRedirect(reverse('portfolio:tfcs'))


@login_required
def nova_noticia_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form_c = NoticiaForm(request.POST or None, request.FILES)

    if form_c.is_valid():
        form_c.save()
        return HttpResponseRedirect(reverse('portfolio:noticias'))

    context = {'form': form_c}
    return render(request, 'portfolio/addNoticia.html', context)


@login_required
def view_editar_noticia(request, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    form = NoticiaForm(request.POST or None, instance=noticia)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:noticias'))

    context = {'form': form, 'noticia_id': noticia_id}
    return render(request, 'portfolio/editNoticia.html', context)


@login_required
def view_apagar_noticia(request, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    noticia.delete()
    return HttpResponseRedirect(reverse('portfolio:noticias'))
