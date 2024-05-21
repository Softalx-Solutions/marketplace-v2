"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import environ
env = environ.Env()
environ.Env.read_env()
from django.contrib import messages

import cloudinary
import cloudinary.uploader
import cloudinary.api


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(",")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #startapps
    'accounts',
    'marketplace',
    'mutual',
    'users',
    'lighthouse',
    
    #third party apps
    'cloudinary',
    'crispy_forms',
    'storages',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'

# adding config
# cloudinary.config( 
#   cloud_name = os.environ['CLOUD_NAME'], 
#   api_key = os.environ['CLOUD_API_KEY'], 
#   api_secret = os.environ['CLOUD_API_SECRET'], 
# )

# register template
TEMPLATE_CONTEXT_PROCESSORS = [
    'django_settings_export.settings_export',
]
FAVI_LOGO = os.environ['FAVI_LOGO']
FRONT_LOGO = os.environ['FRONT_LOGO']
SITE_LOGO = os.environ['SITE_LOGO']
SITE_LOGO_DARK = os.environ['SITE_LOGO_DARK']
DOMAIN_NAME = os.environ['DOMAIN_NAME']
SITE_EMAIL = os.environ['SITE_EMAIL']
SITE_NUMBER = os.environ['SITE_NUMBER']
SITE_ADDRESS = os.environ['SITE_ADDRESS']
SITE_LIVE_CHAT = os.environ['SITE_LIVE_CHAT']

SETTINGS_EXPORT = [
    'FAVI_LOGO',
    'FRONT_LOGO',
    'SITE_LOGO',
    'SITE_LOGO_DARK',
    'DOMAIN_NAME',
    'SITE_EMAIL',
    'SITE_NUMBER',
    'SITE_ADDRESS',
    'SITE_LIVE_CHAT',
]

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = os.environ['EMAIL_PORT']
# EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']
SEND_EMAIL_NAME = os.environ['SEND_EMAIL_NAME']
EMAIL_USE_SSL = os.environ['EMAIL_USE_SSL']


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = '127.0.0.1'
# EMAIL_PORT = 1025

if DEBUG:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/') 
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
    MEDIA_URL = '/media/'
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/') 
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
    MEDIA_URL = '/media/'

    # AWS CONFIG
    AWS_ACCESS_KEY_ID=os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY=os.environ['AWS_SECRET_ACCESS_KEY']



    # Basic Storage configuration for Amazon S3 (Irrespective of Django versions)


    AWS_STORAGE_BUCKET_NAME = 'bazeart-s3-bucket' # - Enter your S3 bucket name HERE

    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    AWS_S3_FILE_OVERWRITE = False

    # Django < 4.2


    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'




    # Django 4.2 >

    '''
    STORAGES = {

        # Media file (image) management   
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
        },
        
        # CSS and JS file management
        "staticfiles": {
            "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
        },
    }

    '''