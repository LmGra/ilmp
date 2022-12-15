#from django.contrib.auth.decorators import login_required
from ilmp_app.decorators import check_pet_owner
from django.utils.decorators import method_decorator

from ilmp_app.forms import MascotasForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from ilmp_app.models import User ,Mascotas, Encuentros, Perdidos
from django.urls import reverse_lazy

from .forms import NewUserForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#Página de inicio
def index(request):
    return render(request,"index.html")

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy(index)

#Mascotas
def creamascota(request):
    if request.method=="POST":
        var_mascota = MascotasForm(data=request.POST)
        if var_mascota.is_valid():
            print(request.user)
            usuario=User.objects.filter(pk=request.user.id)
            #print(usuario.username)
            mascota=var_mascota.save(commit=False)
            mascota.usrPet=request.user
            mascota.save()
            return redirect('mascotas-list')
    else:
        var_mascota=MascotasForm()
    return render(request,"ilmp_app/mascotas_form.html",{"var_mascota":var_mascota})

def listamascota(request):
    listamascota=Mascotas.objects.filter(usrPet=request.user)
    return render(request,"ilmp_app/mascotas_list.html",{"listamascota":listamascota})

#class MascotasListView(LoginRequiredMixin,ListView):
#    model = Mascotas

@method_decorator(check_pet_owner,name='dispatch')
class MascotasDetailView(LoginRequiredMixin,DetailView):
    model = Mascotas

#class MascotasCreateView(LoginRequiredMixin,CreateView):
#    model = Mascotas
#    fields = ['namePet', 'infoPet', 'agePet', 'typePet', 'imgPet', 'genderPet']
#    success_url = reverse_lazy('mascotas-list')

@method_decorator(check_pet_owner,name='dispatch')
class MascotasUpdateView(LoginRequiredMixin,UpdateView):
    model = Mascotas
    fields = ['namePet', 'infoPet', 'agePet', 'typePet', 'imgPet', 'genderPet']
    template_name_sufix = '_update_form'
    success_url = reverse_lazy('mascotas-list')

@method_decorator(check_pet_owner,name='dispatch')
class MascotasDeleteView(LoginRequiredMixin,DeleteView):
    model = Mascotas
    success_url = reverse_lazy('mascotas-list')
    
#Encontradas

class EncuentrosListView(ListView):
    model = Encuentros

class EncuentrosDetailView(DetailView):
    model = Encuentros

class EncuentrosCreateView(CreateView):
    model = Encuentros
    fields = ['typeFind', 'infoFind', 'genderFind', 'ubiFind']
    success_url = reverse_lazy('encuentros-list')

class EncuentrosUpdateView(UpdateView):
    model = Encuentros
    fields = ['typeFind', 'infoFind', 'genderFind', 'ubiFind']
    template_name_sufix = '_update_form'

class EncuentrosDeleteView(DeleteView):
    model = Encuentros
    success_url = reverse_lazy('encuentros-list')

#Buscadas

class PerdidosListView(ListView):
    model = Perdidos

class PerdidosDetailView(DetailView):
    model = Perdidos

class PerdidosCreateView(CreateView):
    model = Perdidos
    fields = ['infoLost', 'dateLost', 'petLost', 'ubiLost']
    success_url = reverse_lazy('perdidos-list')

class PerdidosUpdateView(UpdateView):
    model = Perdidos
    fields = ['infoLost', 'dateLost', 'petLost', 'ubiLost']
    template_name_sufix = '_update_form'

class PerdidosDeleteView(DeleteView):
    model = Perdidos
    success_url = reverse_lazy('perdidos-list')
    
#RegisterRequest
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registro completado." )
			return redirect("main:home")
		messages.error(request, "Fallo en el registro, informacion invalida.")
	form = NewUserForm()
	return render (request=request, template_name="/register.html", context={"register_form":form})

