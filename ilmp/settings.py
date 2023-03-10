"""
Django settings for ilmp project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import ldap
from django_auth_ldap.config import LDAPSearch


from pathlib import Path
import os
#import django_google_maps

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#GOOGLE_MAPS_API_KEY='AIzaSyBDcDUoRlMQqyF3Qobuto6U14RKhRqaNRY'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@d07-(+ml$8l8$=t28thp)7_pd6ngk_13!okiv2@z-5e6k74j0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'ilmp_app.User'

WAGTAIL_SITE_NAME = 'wagtail_app'



# Application definition

INSTALLED_APPS = [
    'ilmp_app.apps.IlmpAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_extensions',

    'blog.apps.BlogAppConfig',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail',

    'modelcluster',
    'taggit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.contrib.redirects.middleware.RedirectMiddleware',

]

ROOT_URLCONF = 'ilmp.urls'

#############LDAP###########

#import ldap
#from django_auth_ldap.config import LDAPSearch


# Baseline configuration.
AUTH_LDAP_SERVER_URI = "ldap://127.0.0.1:1389"

AUTH_LDAP_BIND_DN = "cn=admin,dc=example,dc=org"




AUTH_LDAP_BIND_PASSWORD = "adminpassword"
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "ou=users,dc=example,dc=org", ldap.SCOPE_SUBTREE, "(uid=%(user)s)"
)

#AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
#    "ou=django,ou=groups,dc=example,dc=org",
#    ldap.SCOPE_SUBTREE,
#    "(objectClass=groupOfNames)",
#)
# Populate the Django user from the LDAP directory.



AUTH_LDAP_USER_ATTR_MAP = {
    "email": "mail",
}

AUTHENTICATION_BACKENDS = (
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ilmp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
#	'ENGINE': 'django.db.backends.postgresql_psycopg2',
#	'NAME': 'ilmp',
#	'USER': 'ilmpuser',
#	'PASSWORD': 'ilmpuser',
#	'HOST': 'localhost',
#	'PORT': '',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ilmp',
      	'USER': 'ilmpuser',
        'PASSWORD': 'ilmpuser',
        'HOST': 'ilmpdb-1.ci5gitzmjdfr.us-east-1.rds.amazonaws.com',
        'PORT': '',


    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR,'static'),
#)

#STATIC_ROOT = os.path.join(BASE_DIR,"static/")

#STATICFILES_DIRS=[
#    os.path.join(BASE_DIR,"static"),
#]

#STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_env","static_root")



LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Api
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/var/www/correo' # change this to a proper location