import datetime

from django.shortcuts import render


# Create your views here.

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
