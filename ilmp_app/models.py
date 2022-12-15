from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
#from django.conf import settings


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

#Usuarios
class User(AbstractUser):
    
    nameUsr = models.CharField(max_length=200)
    genderUsr = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    birthUsr = models.DateField(null=True)
    telUsr= models.CharField(max_length = 9)
    imgUsr = models.ImageField(null=True, blank=True, upload_to="images/")
    ubiUsr = models.CharField(max_length=200)
    
    def get_absolute_url(self):
        return reverse('user-list', args=[self.pk])
#    def __str__(self):
#        return self.nameUsr

    
class Mascotas(models.Model):
    namePet = models.CharField(max_length=200)
    infoPet = models.CharField(max_length=200)
    agePet = models.DateField(blank=True, null=True)
    typePet = models.CharField(max_length=200)
    imgPet = models.ImageField(null=True, blank=True, upload_to="images/")
    genderPet = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    #usrPet = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    usrPet = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.namePet
#    def get_absolute_url(self):
#        return reverse('ilmp:mascotas-list')

class Perdidos(models.Model):
    infoLost = models.CharField(max_length=200)
    dateLost = models.DateTimeField(blank=True, null=True)
    petLost = models.ForeignKey("Mascotas", on_delete=models.CASCADE, null=True)
    ubiLost = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.infoLost
    
class Encuentros(models.Model):
    typeFind = models.CharField(max_length=200)
    imgFind = models.ImageField(null=True, blank=True, upload_to="images/")
    infoFind = models.CharField(max_length=200)
    genderFind = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    ubiFind = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.typeFind