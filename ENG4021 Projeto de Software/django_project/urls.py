"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from appdobruno import views

urlpatterns = [
    path('users/login/', views.login_user, name="login"),
    path('users/logout/', views.logout_user, name="logout"),
    path('users', views.create_user),
    # path('users/', include('django.contrib.auth.urls')),
    path('', views.home, name="home"),  
    path('pontosturisticos', views.create_pontosturisticos),
    path('pontosturisticos/update/<id>', views.update_pontosturisticos),
    path('pontosturisticos/delete/<id>', views.delete_pontosturisticos),
    path('cuidadosdicas', views.create_cuidadosdicas),
    path('cuidadosdicas/update/<id>', views.update_cuidadosdicas),
    path('cuidadosdicas/delete/<id>', views.delete_cuidadosdicas),
    path('admin/', admin.site.urls),

]