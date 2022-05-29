from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.index_view, name='index'),
    path('/home', views.home_page_view, name='home'),
    path('/licenciatura', views.lic_page_view, name='licenciatura'),
    path('/formação', views.formac_page_view, name='formação'),
    path('/projetos', views.proj_page_view, name='projetos'),
    path('/apresentação', views.apr_page_view, name='apresentação'),
    path('/competencias', views.comp_page_view, name='competencias'),

]
