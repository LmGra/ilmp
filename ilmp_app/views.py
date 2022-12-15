from django.shortcuts import render
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

class MascotasListView(ListView):
    model = Mascotas

class MascotasDetailView(DetailView):
    model = Mascotas

class MascotasCreateView(CreateView):
    model = Mascotas
    fields = ['namePet', 'infoPet', 'agePet', 'typePet', 'imgPet', 'genderPet', 'usrPet']
    success_url = reverse_lazy('mascotas-list')

class MascotasUpdateView(UpdateView):
    model = Mascotas
    fields = ['namePet', 'infoPet', 'agePet', 'typePet', 'imgPet', 'genderPet', 'usrPet']
    template_name_sufix = '_update_form'
    success_url = reverse_lazy('mascotas-list')

class MascotasDeleteView(DeleteView):
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

