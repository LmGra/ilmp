from django.http import HttpResponse
from ilmp_app.models import Mascotas

def check_pet_owner(func):
    def check_and_call(request, *args, **kwargs):
        pk = kwargs["pk"]
        mascotas = Mascotas.objects.get(pk=pk)
        if not (mascotas.usrPet.id == request.user.id): 
            return HttpResponse("No puedes acceder a este sitio, no tienes permiso.", status=403)
        return func(request, *args, **kwargs)
    return check_and_call