"""ilmp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from ilmp_app import views
from ilmp_app.api import router
from django.conf.urls.static import static
from django.conf import settings

#----------------------WAGTAIL
#
#
from django.urls import path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    #Admin
    path(r'admin/', admin.site.urls),
    
    #Index
    #path(r'', include('ilmp_app.urls')),
    path('', include(('ilmp_app.urls','ilmp'),namespace="ilmp")),
    
    #Accounts
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register_request, name="register"),

    #####################WAGTAIL###############
    
    path('cms/', include(wagtailadmin_urls)),
    path('blog/', include(wagtail_urls)),
    #path('documents/', include(wagtaildocs_urls)),
    #path('pages/', include(wagtail_urls)),

    ###############################################
    
    #Api
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
