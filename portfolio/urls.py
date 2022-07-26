from django.urls import path
from . import views
from .views import BlogView, BlogDetail, AddBlog, UpdateBlog, DeleteBlog, login_user, logout_user, lista_cadeiras, lista_projetos

app_name = "portfolio"

urlpatterns = [
    path('home/', views.index_view, name='home'),
    path('licenciatura/', views.lista_cadeiras, name='licenciatura'),
    path('formação/', views.formac_page_view, name='formação'),
    path('projetos/', views.lista_projetos, name='projetos'),
    path('apresentação/', views.apr_page_view, name='apresentação'),
    path('competencias/', views.comp_page_view, name='competencias'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/article/<int:pk>', BlogDetail.as_view(), name='blog-details'),
    path('blog/add_blog/', AddBlog.as_view(), name='add_blog'),
    path('blog/edit/<int:pk>', UpdateBlog.as_view(), name='edit_blog'),
    path('blog/delete/<int:pk>', DeleteBlog.as_view(), name='delete_blog'),
    path('quizz/', views.quizz_view, name='main-view'),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
]
