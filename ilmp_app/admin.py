from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

#from django_google_maps import widgets as map_widgets
#from django_google_maps import fields as map_fields

#class RentalAdmin(admin.ModelAdmin):
#    formfield_overrides = {
#        map_fields.AddressField:{'widget': map_widgets.GoogleMapsAddressWidget},
#    }


admin.site.register(Mascotas)
admin.site.register(Perdidos)
admin.site.register(Encuentros)
admin.site.register(User)
admin.site.register(Correo)

