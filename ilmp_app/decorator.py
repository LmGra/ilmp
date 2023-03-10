from django.http import HttpResponse
from ilmp_app.models import Mascotas, Perdidos, Encuentros

def check_pet_owner(func):
    def check_and_call(request, *args, **kwargs):
        pk = kwargs["pk"]
        mascotas = Mascotas.objects.get(pk=pk)
        if not (mascotas.usrPet.id == request.user.id): 
            return HttpResponse("No puedes acceder a este sitio, no tienes permiso.", status=403)
        return func(request, *args, **kwargs)
    return check_and_call

def check_lost_owner(func):
    def check_and_call(request, *args, **kwargs):
        pk = kwargs["pk"]
        perdidos = Perdidos.objects.get(pk=pk)
        print(perdidos.petLost.usrPet.id)
        if not (perdidos.petLost.usrPet.id == request.user.id): 
            return HttpResponse("No puedes acceder a este sitio, no tienes permiso.", status=403)
        return func(request, *args, **kwargs)
    return check_and_call

def check_find_owner(func):
    def check_and_call(request, *args, **kwargs):
        pk = kwargs["pk"]
        encuentros = Encuentros.objects.get(pk=pk)
        if not (encuentros.id == request.user.id): 
            return HttpResponse("No puedes acceder a este sitio, no tienes permiso.", status=403)
        return func(request, *args, **kwargs)
    return check_and_call