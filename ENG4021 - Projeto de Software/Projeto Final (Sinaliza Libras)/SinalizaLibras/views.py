from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Videos


# Create your views here.
def home(request):
  return render(request, "home.html")

def aboutUs(request):
  return render(request, "aboutUs.html")

#@login_required
def quizes(request):
  return render(request, "quiz/quizes.html")

#@login_required
def videoAulas(request):
  return render(request, "videoAulas.html")

def base(request):
  return render(request, "base.html")

def loginPage(request):
  return render(request, "login.html")

def logged_out(request):
  return render(request, "logged_out.html")

def password_reset_form(request):
  return render(request, "password_reset_form.html")

def password_reset_done(request):
  return render(request, "password_reset_done.html")

def password_reset_email(request):
  return render(request, "password_reset_email.html")

def password_reset_confirm(request):
  return render(request, "password_reset_confirm.html")

def password_reset_complete(request):
  return render(request, "password_reset_complete.html")

def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
    user.save()
    return redirect ("login")
  return render(request, "register.html", context={"action": "Adicionar"})

'''def login_user(request):
  if request.method == "POST":
    user = authenticate(username = request.POST["username"], password = request.POST['password'])
    if user != None:
      login(request, user)
    else:
      return render(request, "login.html", context={"error_msg": "Usuário não existe"})
    if request.user.is_authenticated:
      return redirect("home")
    return render(request, "login.html", context={"error_msg": "Usuário não pôde ser autenticado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")'''
