"""
Django settings for swatapps project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from unipath import Path
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = Path(__file__).ancestor(3)
SETTINGS_DIR = os.path.dirname(__file__)
TMP_DIR = '/tmp'

sys.path.insert(0, os.path.join(BASE_DIR, 'settings'))
import settings_secret

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = settings_secret.get_secret_key()

# Google recaptcha site/secret keys
NORECAPTCHA_SITE_KEY = settings_secret.get_norecaptcha_site_key()
NORECAPTCHA_SECRET_KEY = settings_secret.get_norecaptcha_secret_key()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SESSION_COOKIE_AGE = 1800
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True

ALLOWED_HOSTS = []

ADMINS = [('Ben Hancock', 'hancocb@purdue.edu')]

AUTH_USER_MODEL = 'swatusers.SwatUser'

FILE_UPLOAD_PERMISSIONS = '0o644'
MAX_UPLOAD_SIZE = '2684354560'

LOGIN_URL = '/login'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'swatusers',
    'swatluu',
    'luuchecker',
    'uncertainty',
    'fieldswat'
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

ROOT_URLCONF = 'swatapps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\', '/')],
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

WSGI_APPLICATION = 'swatapps.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': SETTINGS_DIR + '/my.cnf',
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Media files

MEDIA_ROOT = BASE_DIR
MEDIA_URL = '/media/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = PROJECT_DIR + '/static/'
STATIC_URL = '/static/'
STATIC_PATH = '/static/'
STATIC_PATH_DIR = os.path.join(PROJECT_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static_storage'),
)


# Email

EMAIL_USE_TLS = True
EMAIL_HOST = settings_secret.get_email_host()
EMAIL_HOST_USER = settings_secret.get_email_user()
EMAIL_HOST_PASSWORD = settings_secret.get_email_password()
EMAIL_PORT = settings_secret.get_email_port()
DEFAULT_FROM_EMAIL = settings_secret.get_email_user()


# API Key

APIKEY = settings_secret.get_apikey()