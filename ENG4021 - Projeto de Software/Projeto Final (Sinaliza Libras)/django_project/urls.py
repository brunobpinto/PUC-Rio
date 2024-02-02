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
from SinalizaLibras import views

urlpatterns = [
    #path('users/login/', views.login_user, name="login"),
    #path('users/logout/', views.logout, name="logout"),
    path('register', views.create_user),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home),
    path('base', views.base),
    path('login', views.loginPage),
    path('logout', views.logout), 
    path('password_reset_form', views.password_reset_form),
    path('password_reset_done', views.password_reset_done),
    path('password_reset_email', views.password_reset_email),
    path('password_reset_confirm', views.password_reset_confirm),
    path('password_reset_complete', views.password_reset_complete),
    path('admin/', admin.site.urls),
    path('quizes', views.quizes),
    path('videoAulas', views.videoAulas),
    path('sobreNos/', views.aboutUs),
    path('admin/', admin.site.urls),
]
