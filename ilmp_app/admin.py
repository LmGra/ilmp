from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

admin.site.register(Mascotas)
admin.site.register(Perdidos)
admin.site.register(Encuentros)
admin.site.register(User)

