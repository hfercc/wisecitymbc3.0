"""
Django settings for wisecitymbc project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%^^u0c@yf3^0#it=*xw=0akolja1&k3!m*#n)zci-m_z=zzz78'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'enhancements.rest.apps.AutoDiscoverConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Enhancements
    'enhancements.constants',
    'enhancements.postgres',
    # Third-party
    'watson',
    'django_nose',
    'django_object_actions',
    'webpack_loader',
    'rules.apps.AutodiscoverRulesConfig',
    # website related apps
    'accounts',
    'articles',
    'questions',
    'notifications',
    'files',
    'finance',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wisecitymbc.urls'

CONTEXT_PROCESSORS = [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': CONTEXT_PROCESSORS,
        },
    },
    {
        'BACKEND': 'enhancements.jinja2.backends.Jinja2Backend',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'enhancements.jinja2.env.environment',
            'context_processors': CONTEXT_PROCESSORS,
            'extensions': [
                'webpack_loader.contrib.jinja2ext.WebpackExtension'
            ]
        },
    },
]

WSGI_APPLICATION = 'wisecitymbc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'app_wisecitymbc',
        'USER': 'wisecity',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'accounts.User'

AUTHENTICATION_BACKENDS = [
    'rules.permissions.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    'front-end/dest'
]

# Configuration for django-webpack-loader.

FRONTEND_DIR = os.path.join(BASE_DIR, 'front-end')

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': './',
        'STATS_FILE': os.path.join(FRONTEND_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': ['.+\.hot-update.js', '.+\.map']
    }
}

# Tests

TEST_RUNNER = 'enhancements.postgres.test.PostgresEnhancedTestRunner'
NOSE_ARGS = ['--nocapture',
             '--nologcapture', ]

# rest_framework
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'enhancements.rest.renderers.JSONRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'enhancements.rest.permissions.DjangoObjectPermissionOrAnonReadOnly',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.CursorPagination',
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'PAGE_SIZE': 10,
}


# watson: full text search engine

WATSON_BACKEND = 'enhancements.postgres.search_backends'\
    '.PostgresChineseSearchBackend'

TS_CONFIG_NAME = 'chinesecfg'

from .qiniu_keys import *

QINIU_BUCKET_NAME = 'wisecitymbc'
QINIU_DOMAIN_NAME = '7xkade.dl1.z0.glb.clouddn.com'

CONSTS_OUTPUT_PATHS = [
    'front-end/consts.json'
]