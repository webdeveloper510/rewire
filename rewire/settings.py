"""
Django settings for rewire project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from decimal import DefaultContext
from pathlib import Path
import pymysql
pymysql.version_info = (1, 4, 13, "final", 0)

pymysql.install_as_MySQLdb()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-em1o&6n19_mp)&6xl!39zq7nh441z-7%&qwnu2vrq8b#-4$n2z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

import os
from django.contrib.messages import constants as messages


MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }
    

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['184.168.122.169']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'google_translate',
    'crispy_forms',
    'active_link',
   
]

AUTH_USER_MODEL = 'app.user'

MIDDLEWARE = [
    "app.middelware.ForceDefaultLanguageMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware', 
    
  
   
]

ROOT_URLCONF = 'rewire.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'rewire.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
print(LOCALE_PATHS)

# DATABASES = {
#     'default': {
#        'ENGINE': 'django.db.backends.mysql',   
#        'NAME': 'rewire',
#        'HOST': 'localhost',
#        'PORT': '3306',
#        'USER': 'root',
#        'PASSWORD': '',
#        'OPTIONS': {
#             'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
            
             
#         }
#     }
# }


DATE_FORMAT = 'YYYY-MM-DD'

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.mysql',   
       'NAME': 'rewire',
       'HOST': 'localhost',
       'PORT': '3306',
       'USER': 'rewire',
       'PASSWORD': 'Hg2gi37#',
       'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
            
             
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/


from django.utils.translation import  gettext_lazy as _

LANGUAGE_CODE = 'pt'

DEFAULT_LANGUAGE = 2
LANGUAGES = (
    ('en-us', 'English'),
    ('pt', 'Portuguese'),
    
    
   
   
)

from django.conf import settings

print("check1",settings.LANGUAGE_CODE)

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'staticfiles'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'testsood981@gmail.com'
EMAIL_HOST_PASSWORD = 'jivyydbevbsscuoi'
EMAIL_PORT = 587


