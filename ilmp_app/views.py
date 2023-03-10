#from django.contrib.auth.decorators import login_required
from django.db.models import Q

from ilmp_app.decorator import check_pet_owner, check_lost_owner, check_find_owner
from django.utils.decorators import method_decorator

from ilmp_app.forms import MascotasForm, PerdidosForm, EncuentrosForm, CorreoForm
# arriba , CorreoForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from ilmp_app.models import Correo, User ,Mascotas, Encuentros, Perdidos
from django.urls import reverse_lazy, reverse

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
    success_url = reverse_lazy('ilmp:user-list')

class UserListView(ListView):
    model = User

#Mascotas
def creamascota(request):
    if request.method=="POST":
        var_mascota = MascotasForm(request.POST, request.FILES)
        if var_mascota.is_valid():
            print(request.user)
            usuario=User.objects.filter(pk=request.user.id)
            #print(usuario.username)
            mascota=var_mascota.save(commit=False)
            mascota.usrPet=request.user
            mascota.save()
            return redirect('ilmp:mascotas-list')
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
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('ilmp:mascotas-list')

@method_decorator(check_pet_owner,name='dispatch')
class MascotasDeleteView(LoginRequiredMixin,DeleteView):
    model = Mascotas
    success_url = reverse_lazy('ilmp:mascotas-list')
    
#Encontradas

class EncuentrosListView(ListView):
    model = Encuentros

class EncuentrosDetailView(DetailView):
    model = Encuentros

#class EncuentrosCreateView(CreateView):
#    model = Encuentros
#    fields = ['typeFind', 'imgFind', 'infoFind', 'genderFind', 'ubiFind']
#    success_url = reverse_lazy('ilmp:encuentros-list')

def createEncuentros(request):
    if request.method == "POST":
        encuentros_form = EncuentrosForm(data=request.POST, files=request.FILES)
        if encuentros_form.is_valid():
            encuentros = encuentros_form.save(commit=False)
            encuentros.usrLost = request.user
            encuentros.save()
            return redirect('ilmp:encuentros-list')
    else:
        encuentros_form = EncuentrosForm()
        
    return render(request, "ilmp_app/encuentros_form.html", {"encuentros_form":encuentros_form})

@method_decorator(check_find_owner,name='dispatch')
class EncuentrosUpdateView(UpdateView):
    model = Encuentros
    fields = ['typeFind', 'imgFind', 'infoFind', 'genderFind', 'ubiFind']
    template_name_sufix = '_update_form'

@method_decorator(check_find_owner,name='dispatch')
class EncuentrosDeleteView(DeleteView):
    model = Encuentros
    success_url = reverse_lazy('ilmp:encuentros-list')


#Perdidos
class PerdidosListView(ListView):
    model = Perdidos

class PerdidosDetailView(DetailView):
    model = Perdidos

def creaperdidos(request):
    #var_perdidos = PerdidosForm()
    var_ownpet = Mascotas.objects.filter(usrPet=request.user)
    if request.method=="POST":
        var_perdidos = PerdidosForm(request.POST)
        print(request.POST)
        #var_mascota=Mascotas.objects.get(pk=request.POST.get('pet'))
        #var_perdidos.petLost=var_mascota
       
        #var_perdidos.__setattr__("petLost",request.POST.get('pet',''))
        if var_perdidos.is_valid():
            form = var_perdidos.save(commit=False)
            print("AAAA")
            var_mascota=Mascotas.objects.get(pk=request.POST.get('pet'))
            #var_petlost = Perdidos.objects.create()
            #var_petlost.infoLost=request.POST.get('infoLost','')
            #var_petlost.dateLost=request.POST.get('dateLost','')
            form.petLost=var_mascota
            print(form.petLost, form.infoLost, form.dateLost, form.ubiLost)
            form.save()
            #var_petlost.ubiLost=request.POST.get('ubiLost','')
            return redirect(reverse('ilmp:perdidos-list'))
    else:
        var_perdidos = PerdidosForm()
    return render(request,"ilmp_app/perdidos_form.html",{'var_perdidos':var_perdidos,'ownpet':var_ownpet})
        
#def creaperdidos(request):
#    if request.method=="POST":
#        var_perdidos = PerdidosForm(request.POST)
#        if var_perdidos.is_valid():
#            print(request.user)
#            usuario=User.objects.filter(pk=request.user.id)
#            #print(usuario.username)
#            perdidos=var_perdidos.save(commit=False)
#            perdidos.petLost.usrPet=request.user
#            perdidos.save()
#            return redirect('ilmp:perdidos-list')
#    else:
#        var_perdidos=PerdidosForm()
#    return render(request,"ilmp_app/perdidos_form.html",{"var_perdidos":var_perdidos})



#class PerdidosCreateView(CreateView):
#    model = Perdidos
#    fields = ['infoLost', 'dateLost', 'petLost', 'ubiLost']
#    success_url = reverse_lazy('ilmp:perdidos-list')

@method_decorator(check_lost_owner,name='dispatch')
class PerdidosUpdateView(UpdateView):
    model = Perdidos
    fields = ['infoLost', 'dateLost', 'petLost', 'ubiLost']
    template_name_sufix = '_update_form'

@method_decorator(check_lost_owner,name='dispatch')
class PerdidosDeleteView(DeleteView):
    model = Perdidos
    success_url = reverse_lazy('ilmp:perdidos-list')
    
    
#Correo
def createCorreo(request,pk):
    if request.method == "POST":
        correo_form = CorreoForm(data=request.POST)
        if correo_form.is_valid():
            correo = correo_form.save(commit=False)
            correo.remitente = request.user
            correo.destinatario = User.objects.get(pk=pk)
            correo.save()
            return redirect('ilmp:encuentros-list')
    else:
        correo_form = CorreoForm()
        
    return render(request, "ilmp_app/correo_form.html", {"correo_form":correo_form})

def correoRecivido(request):
    correo_list = Correo.objects.filter(destinatario=request.user)
    return render(request, "ilmp_app/correo_recivido.html",{"correo_recivido":correo_list})

def correoEnviado(request):
    correo_list = Correo.objects.filter(remitente=request.user)
    return render(request, "ilmp_app/correo_enviado.html",{"correo_enviado":correo_list})

    
#Buscador
class search(ListView):
    model = Perdidos
    template_name="search.html"
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list=Perdidos.objects.filter(Q(petLost__in=[query]))
        return object_list
    
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

