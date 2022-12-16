##Api

from django.contrib.auth.models import User
from ilmp_app.models import *
from rest_framework import routers, serializers, viewsets

###Usuarios

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

###Mascotas

# Serializers define the API representation.
class MascotasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mascotas
        fields = ['url', 'namePet', 'infoPet', 'agePet', 'typePet', 'imgPet', 'genderPet', 'usrPet']

# ViewSets define the view behavior.
class MascotasViewSet(viewsets.ModelViewSet):
    queryset = Mascotas.objects.all()
    serializer_class = MascotasSerializer

####Perdidos

# Serializers define the API representation.
class PerdidosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perdidos
        fields = ['infoLost', 'dateLost', 'petLost', 'ubiLost']

# ViewSets define the view behavior.
class PerdidosViewSet(viewsets.ModelViewSet):
    queryset = Perdidos.objects.all()
    serializer_class = PerdidosSerializer

###Encuentros

# Serializers define the API representation.
class EncuentrosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Encuentros
        fields = ['typeFind','imgFind', 'infoFind', 'genderFind', 'ubiFind']

# ViewSets define the view behavior.
class EncuentrosViewSet(viewsets.ModelViewSet):
    queryset = Encuentros.objects.all()
    serializer_class = EncuentrosSerializer

#Api Reg
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'mascotas', MascotasViewSet)
router.register(r'perdidos', PerdidosViewSet)
router.register(r'encuentros', EncuentrosViewSet)