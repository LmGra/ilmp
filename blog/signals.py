from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from django.contrib.auth.signals import user_logged_in
from ilmp_app.models import User
from django.core.mail import send_mail
from django.dispatch import receiver

@receiver(user_logged_in)
def log_user_loggin(sender, user, **kwargs):
    
    u=User.objects.get(username=user)
    g=Group.objects.get(name='Blogger')
    c=User.objects.get(username=user).email
    
    if g in u.groups.all():
        print("Este usuario ya pertenece al grupo Blogger")
    else:
        print("Añadiendo el usuario al grupo Blogger")
        send_mail(
            'Subject',
            'Message',
            'from@example.com',
            [c],
            fail_silently=False,
        )
    
    
#    try:
#        u = User.objects.get(username=user)
#        g = Group.objects.get(name='Blogger')
#        c = User.objects.get(username=user).email
         
#        if g in u.groups.all():
#            print(f"{u.username} Ya pertenece al grupo.")

#        else:
#            print(f"{u.username} Añadiendo el usuario al grupo Blogger")
#            u.groups.add(g)
#            send_mail(
#                'Subject',
#                'Message.',
#                'from@example.com',
#                [c],
#                fail_silently=False,
#            )
#    except:
#        print("El usuario introducido no existe")
