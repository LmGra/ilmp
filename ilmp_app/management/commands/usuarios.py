from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from django.contrib.auth.signals import user_logged_in
from ilmp_app.models import User

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('usuario', type=str, help='Introduce el usuario a meter en Bloggers')

    def handle(self, *args, **kwargs):
        try:
            nombre = kwargs['usuario']
            u = User.objects.get(username=nombre)
            g = Group.objects.get(name='Blogger')
            if g in u.groups.all():
                print(f"{u.username} Ya pertenece al grupo.")

            else:
                print(f"{u.username} Añadiendo el usuario al grupo Blogger")
                u.groups.add(g)
        except:
            print("El usuario introducido no existe")
