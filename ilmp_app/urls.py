from django.urls import path
#from django.conf.urls import include
from ilmp_app.views import index, search, listamascota, creamascota, UserCreateView, EncuentrosDeleteView, EncuentrosUpdateView, EncuentrosCreateView, PerdidosUpdateView, PerdidosDeleteView, PerdidosCreateView ,MascotasDeleteView, MascotasUpdateView, PerdidosDetailView, EncuentrosDetailView, MascotasDetailView, EncuentrosListView, PerdidosListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'',index),
    
    #Mascotas
    path('mascotas/', listamascota, name='mascotas-list'),
    #path('mascotas/', MascotasListView.as_view(), name='mascotas-list'),
    path('mascotas/<int:pk>/', MascotasDetailView.as_view(), name='mascotas-detail'),
    path("mascotas/add/", creamascota, name='mascotas-add'),
    #path("mascotas/add/", MascotasCreateView.as_view(), name='mascotas-add'),
    path('mascotas/<int:pk>/edit/', MascotasUpdateView.as_view(), name='mascotas-update'),
    path('mascotas/<int:pk>/delete/', MascotasDeleteView.as_view(), name='mascotas-delete'),
    
    #Encuentros
    path('encuentros/', EncuentrosListView.as_view(), name ='encuentros-list'),
    path('encuentros/<int:pk>/', EncuentrosDetailView.as_view(), name='encuentros-detail'),
    path("encuentros/add/", EncuentrosCreateView.as_view(), name='encuentros-add'),
    path('encuentros/<int:pk>/edit/', EncuentrosUpdateView.as_view(), name='encuentros-update'),
    path('encuentros/<int:pk>/delete/', EncuentrosDeleteView.as_view(), name='encuentros-delete'),

    #Perdidos
    path('perdidos/', PerdidosListView.as_view(), name='perdidos-list'),
    path('perdidos/<int:pk>/', PerdidosDetailView.as_view(), name='perdidos-detail'),
    path("perdidos/add/", PerdidosCreateView.as_view(), name='perdidos-add'),
    path('perdidos/<int:pk>/edit/', PerdidosUpdateView.as_view(), name='perdidos-update'),
    path('perdidos/<int:pk>/delete/', PerdidosDeleteView.as_view(), name='perdidos-delete'),
    
    #Registro
    path("register/", UserCreateView.as_view(), name='user-add'),
    
    #Search
    path('gimnasio/search/', search.as_view(), name="search"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

