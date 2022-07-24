from django.contrib import admin
from django.urls import path, include


app_name = "portfolio"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', include('portfolio.urls')),
    path('portfolio/login/', include("django.contrib.auth.urls")),
]
