from django.urls import path
from . import views
from .views import BlogView, BlogDetail, AddBlog, UpdateBlog, DeleteBlog

app_name = "portfolio"

urlpatterns = [
    path('home/', views.index_view, name='home'),
    path('licenciatura/', views.lista_cadeiras, name='licenciatura'),
    path('projetos/', views.lista_projetos, name='projetos'),
    path('apresentação/', views.apresentacao_view, name='apresentação'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/article/<int:pk>', BlogDetail.as_view(), name='blog-details'),
    path('blog/add_blog/', AddBlog.as_view(), name='add_blog'),
    path('blog/edit/<int:pk>', UpdateBlog.as_view(), name='edit_blog'),
    path('blog/delete/<int:pk>', DeleteBlog.as_view(), name='delete_blog'),
    path('quizz/', views.quizz_view, name='quizz'),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('tfcs/', views.lista_tfcs, name='tfcs'),
    path('noticias/', views.lista_noticias, name='noticias'),
    path('diagramas/', views.diagramas_view, name='diagramas'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('pw/', views.pw_view, name='pw'),
    path('contacto/', views.contacto_view, name='contacto'),

    path('addPessoa/', views.nova_pessoa_page_view, name='addPessoa'),

    path('addProjeto/', views.novo_projetos_page_view, name='addProjeto'),
    path('editProjeto/<int:projeto_id>', views.view_editar_projeto, name='editProjeto'),
    path('apagarProjeto/<int:projeto_id>', views.view_apagar_projeto, name='apagarProjeto'),

    path('addCadeira/', views.nova_cadeira_page_view, name='addCadeira'),
    path('editCadeira/<int:cadeira_id>', views.view_editar_cadeira, name='editCadeira'),
    path('apagarCadeira/<int:cadeira_id>', views.view_apagar_cadeira, name='apagarCadeira'),

    path('addNoticia/', views.nova_noticia_page_view, name='addNoticia'),
    path('editNoticia/<int:noticia_id>', views.view_editar_noticia, name='editNoticia'),
    path('apagarNoticia/<int:noticia_id>', views.view_apagar_noticia, name='apagarNoticia'),

    path('addTFC/', views.novo_tfc_page_view, name='addTFC'),
    path('editTFC/<int:tfc_id>', views.view_editar_tfc, name='editTFC'),
    path('apagarTFC/<int:tfc_id>', views.view_apagar_tfc, name='apagarTFC'),
]
