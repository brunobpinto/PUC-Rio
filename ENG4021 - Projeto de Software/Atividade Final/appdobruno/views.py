from django.shortcuts import render, redirect
from .models import PontosTuristicos, CuidadosDicas
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
  pontos = PontosTuristicos.objects.all()
  cuidados = CuidadosDicas.objects.all()
  
  return render(request, "home.html", context={
    "pontos": pontos,
    "cuidados": cuidados
  
  
  })

# FUNCOES E FORMS PARA PONTOS TURISTICOS
@login_required
def create_pontosturisticos(request):
  if request.method == "POST":
    # Criar um novo ponto turistico usando os valores do meu formulário
    PontosTuristicos.objects.create(
      ponto_turistico = request.POST["ponto_turistico"],
      bairro = request.POST["bairro"],
      cidade = request.POST["cidade"],
      rating = request.POST["rating"]
    )

    return redirect("home")
  return render(request, "forms.html", context={"action": "Adicionar"})

@login_required
def update_pontosturisticos(request, id):
  pontos = PontosTuristicos.objects.get(id = id)
  if request.method == "POST":
    # Criar um novo ponto turistico usando os valores do meu formulário
    pontos.ponto_turistico = request.POST["ponto_turistico"]
    pontos.bairro = request.POST["bairro"]
    pontos.cidade = request.POST["cidade"]
    pontos.rating = request.POST["rating"]
    pontos.save()

    return redirect("home")
  return render(request, "forms.html", context={"action": "Atualizar","pontos": pontos})

@login_required
def delete_pontosturisticos(request, id):
  pontos = PontosTuristicos.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      pontos.delete()

    return redirect("home")
  return render(request, "are_you_sure.html", context={"pontos": pontos})





# FUNCOES E FORMS PARA CUIDADOS E DICAS
@login_required
def create_cuidadosdicas(request):
  if request.method == "POST":
    # Criar um novo ponto turistico usando os valores do meu formulário
    CuidadosDicas.objects.create(
      cuidados = request.POST["cuidados"],
      lugares_para_ter_cuidado = request.POST["lugares_para_ter_cuidado"],
      perigo = request.POST["perigo"])
    return redirect("home")

  #options = CuidadosDicas.cuidados.options

  return render(request, "forms2.html", context={"action": "Adicionar"})

@login_required
def update_cuidadosdicas(request, id):
  cuidados = CuidadosDicas.objects.get(id = id)
  if request.method == "POST":
    # Criar um novo ponto turistico usando os valores do meu formulário
    cuidados.cuidados = request.POST["cuidados"]
    cuidados.lugares_para_ter_cuidado = request.POST["lugares_para_ter_cuidado"]
    cuidados.perigo = request.POST["perigo"]
    cuidados.save()
    return redirect("home")
    
  #options = CuidadosDicas.cuidados.options

  return render(request, "forms2.html", context={
    "action": "Atualizar",
    "cuidados": cuidados
    
  })

@login_required
def delete_cuidadosdicas(request, id):
  cuidados = CuidadosDicas.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      cuidados.delete()

    return redirect("home")
  return render(request, "are_you_sure2.html", context={"cuidados": cuidados})



def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(
      request.POST["username"],
      request.POST["email"], 
      request.POST["password"]
    )
    user.save()
    return redirect("home")
  return render(request, "register.html", context={"action": "Adicionar"})

def login_user(request):
  if request.method == "POST":
    user = authenticate(
      username = request.POST["username"],
      password = request.POST["password"]
    )

    if user != None:
      login(request, user)
    else:
      return render(request, "login.html", context={"error_msg": "Usuário não existe"})
    print(request.user)
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
      return redirect("home")
    return render(request, "login.html", context={"error_msg": "Usuário não pode ser autenticado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")