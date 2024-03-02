import datetime
import os
from pathlib import Path
from dotenv import load_dotenv

import environ

load_dotenv()

env = environ.Env(
    # Django
    DEBUG=bool,
    SECRET_KEY=str,

    # Postgres
    POSTGRES_DB_NAME=str,
    POSTGRES_DB_USER=str,
    POSTGRES_DB_PASSWORD=str,
    POSTGRES_DB_HOST=str,
    POSTGRES_DB_PORT=int,

    # Localhost
    LOCALHOST=str,
    ALLOWED_HOSTS=str,

    # Internal IPS
    INTERNAL_IPS=str,
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(BASE_DIR / '.env.local')
# environ.Env.read_env(BASE_DIR / '.env.docker')
# environ.Env.read_env(BASE_DIR / '.env.example')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

LOCALHOST = env('LOCALHOST')
BASE_URI = "/api/v0"
ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(', ')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 3-d party services
INSTALLED_APPS += [
    # 3-d party apps
    'djoser',
    'rest_framework',
    'rest_framework_swagger',
    'drf_yasg',
    'rest_framework_simplejwt',
    'drf_standardized_errors',
    'corsheaders',
]

# Local Apps
INSTALLED_APPS += [
    'accounts',
    'comments',
    'blog',
    'contacts',
    'projects',
    'biography',
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

ROOT_URLCONF = 'portfolio.urls'

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
            'libraries': {
                'staticfiles': 'django.templatetags.static'
            }
        },

    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("POSTGRES_DB_NAME"),
        'USER': env("POSTGRES_DB_USER"),
        'PASSWORD': env("POSTGRES_DB_PASSWORD"),
        'HOST': env("POSTGRES_DB_HOST"),
        'PORT': env("POSTGRES_DB_PORT"),
    }
}

# Internal IPS
INTERNAL_IPS = env("INTERNAL_IPS").split(", ")

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

# JWT
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=2),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),  # default
    # 'JWT_AUTH_HEADER_PREFIX': 'JWT'
}

# DJOSER
DJOSER = {
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'ACTIVATION_URL': 'auth/activate/{uid}/{token}/',
    'PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'PASSWORD_RESET_CONFIRM_URL': 'auth/reset/confirm/{uid}/{token}/',
    'TOKEN_MODEL': None
}

# Allauth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_USERNAME_BLACKLIST = ["admin", "administrator", "moderator", "DjangoSchool"]
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_REDIRECT_URL = "/"
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True


# CORS
CORS_ALLOWED_ORIGINS = env("CORS_ALLOWED_ORIGINS").split(", ")
CORS_ORIGIN_ALLOW_ALL = bool(env("CORS_ORIGIN_ALLOW_ALL"))


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
