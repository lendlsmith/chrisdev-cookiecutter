# -*- coding: utf-8 -*-
import os
from os.path import join

try:
    from S3 import CallingFormat
    AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
except ImportError:
    pass

from configurations import Configuration, values

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class Common(Configuration):

    ########## APP CONFIGURATION
    DJANGO_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # 'django.contrib.humanize',

        # Admin
        'django.contrib.admin',
    )
    
    THIRD_PARTY_APPS = (
        'south',
    )

    LOCAL_APPS = (
        'users',
        'utils', 
    )

    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    INSTALLED_APPS += (
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
    )
    ########## END APP CONFIGURATION

    ########## MIDDLEWARE CONFIGURATION
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
    ########## END MIDDLEWARE CONFIGURATION

   
    ########## DEBUG
    DEBUG = values.BooleanValue(True)
    TEMPLATE_DEBUG = DEBUG
    ########## END DEBUG

    
    ########## SECRET CONFIGURATION
    SECRET_KEY = "CHANGEME!!!"
    ########## END SECRET CONFIGURATION

    
    ########## FIXTURE CONFIGURATION
    FIXTURE_DIRS = (
        join(BASE_DIR, 'fixtures'),
    )
    ########## END FIXTURE CONFIGURATION

    
    ########## EMAIL CONFIGURATION
    EMAIL_BACKEND = values.Value('django.core.mail.backends.smtp.EmailBackend')
    ########## END EMAIL CONFIGURATION

   
    ########## MANAGER CONFIGURATION
    ADMINS = (('{{cookiecutter.author_name}}', '{{cookiecutter.email}}'),)
    MANAGERS = ADMINS
    ########## END MANAGER CONFIGURATION

   
    ########## DATABASE CONFIGURATION
    DATABASES = values.DatabaseURLValue('postgres://localhost/{{cookiecutter.repo_name}}')
    ########## END DATABASE CONFIGURATION


    ########## CACHING
    CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
        }
    }
    ########## END CACHING


    ########## GENERAL CONFIGURATION
    TIME_ZONE = 'America/Los_Angeles'
    LANGUAGE_CODE = 'en-us'
    SITE_ID = 1
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    ########## END GENERAL CONFIGURATION


    ########## TEMPLATE CONFIGURATION
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        "allauth.account.context_processors.account",
        "allauth.socialaccount.context_processors.socialaccount",
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
    )

    TEMPLATE_DIRS = (
        join(BASE_DIR, 'templates'),
    )

    TEMPLATE_LOADERS = (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )
    ########## END TEMPLATE CONFIGURATION


    ########## STATIC FILE CONFIGURATION
    STATIC_ROOT = join(os.path.dirname(BASE_DIR), 'staticfiles')

    STATIC_URL = '/static/'

    STATICFILES_DIRS = (join(BASE_DIR, 'static'),)

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
    ########## END STATIC FILE CONFIGURATION


    ########## MEDIA CONFIGURATION
    MEDIA_ROOT = join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
    ########## END MEDIA CONFIGURATION


    ########## URL Configuration
    ROOT_URLCONF = 'config.urls'
    WSGI_APPLICATION = 'config.wsgi.application'
    ########## End URL Configuration


    ########## AUTHENTICATION CONFIGURATION
    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
    )

    ACCOUNT_AUTHENTICATION_METHOD = "username"
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_VERIFICATION = "mandatory"
    ########## END AUTHENTICATION CONFIGURATION


    ########## Custom user app defaults
    AUTH_USER_MODEL = "users.User"
    LOGIN_REDIRECT_URL = "users:redirect"
    ########## END Custom user app defaults


    ########## SLUGLIFIER
    AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"
    ########## END SLUGLIFIER


    ########## LOGGING CONFIGURATION
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            }
        },
        'loggers': {
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': True,
            },
        }
    }
    ########## END LOGGING CONFIGURATION


class Local(Common):

    ########## INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    ########## END INSTALLED_APPS


    ########## Mail settings
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 1025
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')
    ########## End mail settings


    ########## django-debug-toolbar
    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)
    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TEMPLATE_CONTEXT': True,
    }
    ########## end django-debug-toolbar


class Production(Common):

    ########## INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    ########## END INSTALLED_APPS


    ########## SECRET KEY
    SECRET_KEY = values.SecretValue()
    ########## END SECRET KEY


    ########## django-secure
    INSTALLED_APPS += ("djangosecure", )


    # set this to 60 seconds and then to 518400 when you can prove it works
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_FRAME_DENY = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SESSION_COOKIE_SECURE = values.BooleanValue(False)
    SESSION_COOKIE_HTTPONLY = values.BooleanValue(True)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)
    ########## end django-secure


    ########## SITE CONFIGURATION
    ALLOWED_HOSTS = ["*"]
    ########## END SITE CONFIGURATION


    INSTALLED_APPS += ("gunicorn", )


    ########## STORAGE CONFIGURATION
    INSTALLED_APPS += (
        'storages',
    )

    STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_ACCESS_KEY_ID = values.SecretValue()
    AWS_SECRET_ACCESS_KEY = values.SecretValue()
    AWS_STORAGE_BUCKET_NAME = values.SecretValue()
    AWS_AUTO_CREATE_BUCKET = True
    AWS_QUERYSTRING_AUTH = False

    AWS_PRELOAD_METADATA = True
    INSTALLED_APPS += ("collectfast", )

    AWS_EXPIREY = 60 * 60 * 24 * 7
    AWS_HEADERS = {
        'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIREY,
            AWS_EXPIREY)
    }

    STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
    ########## END STORAGE CONFIGURATION


    ########## EMAIL
    DEFAULT_FROM_EMAIL = values.Value(
            '{{cookiecutter.project_name}} <{{cookiecutter.project_name}}-noreply@{{cookiecutter.domain_name}}>')
    EMAIL_HOST = values.Value('smtp.sendgrid.com')
    EMAIL_HOST_PASSWORD = values.SecretValue(environ_prefix="", environ_name="SENDGRID_PASSWORD")
    EMAIL_HOST_USER = values.SecretValue(environ_prefix="", environ_name="SENDGRID_USERNAME")
    EMAIL_PORT = values.IntegerValue(587, environ_prefix="", environ_name="EMAIL_PORT")
    EMAIL_SUBJECT_PREFIX = values.Value('[{{cookiecutter.project_name}}] ', environ_name="EMAIL_SUBJECT_PREFIX")
    EMAIL_USE_TLS = True
    SERVER_EMAIL = EMAIL_HOST_USER
    ########## END EMAIL


    ########## TEMPLATE CONFIGURATION
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', 
            ('django.template.loaders.filesystem.Loader',
             'django.template.loaders.app_directories.Loader',
             )
         ),
    )
    ########## END TEMPLATE CONFIGURATION


    ########## CACHING
    CACHES = values.CacheURLValue(default="memcached://127.0.0.1:11211")
    ########## END CACHING