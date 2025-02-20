"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path
from django.contrib.messages import constants as messages
from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")
CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS").split(",")


# Application definition

INSTALLED_APPS = [
     "jazzmin",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'Myapp',
    'CustomUser',

    #3rd party
    'django_ckeditor_5',
    'ckeditor',
    "ckeditor_uploader",
    'easyaudit',
    'widget_tweaks',
    'django_filters',
    "crispy_forms",
    "crispy_bootstrap5",
    "django_htmx",

]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'easyaudit.middleware.easyaudit.EasyAuditMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_htmx.middleware.HtmxMiddleware",

]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DATABASE_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': BASE_DIR / os.getenv('DATABASE_NAME', 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Adjust based on your project structure
]
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Only used in production

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Custom user model
AUTH_USER_MODEL = 'CustomUser.User'



DJANGO_EASY_AUDIT_CHECK_IF_REQUEST_USER_EXISTS = True

# settings.py

# settings.py

# DJANGO_EASY_AUDIT_UNREGISTERED_URLS_DEFAULT = [r'^/admin/', r'^/static/', r'^/favicon.ico$',r'^/login/', r'^/logout/', r'^/register/',r'^/']
DJANGO_EASY_AUDIT_REGISTERED_URLS = [
    r'^/learn/courses/',  # Existing registered URL
    r'^/learn/content/[a-zA-Z0-9-_]+/$',  # New pattern for course detail with a slug
]


MESSAGE_TAGS = {
    messages.DEBUG: 'notify',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'error',
}



JAZZMIN_SETTINGS = {
    "site_title": "My E-Learning Admin",
    "site_header": "E-Learning Admin",
    "welcome_sign": "Welcome to the E-Learning Dashboard",
    "site_brand": "E-Learning",
    "copyright": " E-Learning Platform",
    "search_model": "Myapp.Course",  # Replace 'yourapp' with your actual app name
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},  # Quick access to Users
    ],
    "changeform_format": "horizontal_tabs",  # "horizontal_tabs" or "collapsible"
    "show_ui_builder": True,  # Show UI customization options
    "icons": {
        "CustomUser.User": "fas fa-user",
        "auth.group": "fas fa-users",
        "Myapp.Course": "fas fa-book",  # Customize icons for your models
        "Myapp.VideoEvent": "fas fa-video",
    },
    "custom_css": None,  # Add your custom CSS if needed
    "custom_js": None,  # Add your custom JavaScript if needed
}




CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"  # Path to CKEditor files

CKEDITOR_CONFIGS = {
    'default': {
        'height': 500,  # Editor height
        'width': '100%',  # Editor width
        'toolbar': 'full',  # Full toolbar
        'extraPlugins': ','.join([
            'uploadimage',  # Enables local image uploads
            'filebrowser',  # Enables file browsing
            'image2',  # Advanced image features
            'widget',
            'embed',  # Allows embedding YouTube, Vimeo, etc.
            'embedsemantic',  # Improves embedding structure
            'iframe',  # Allows adding iframes
            'html5video',  # Adds the HTML5 video plugin
        ]),
        'contentsCss': [
            '/static/unfold/css/main.css',  # Apply Unfold's main styles
            '/static/unfold/css/admin.css',  # Apply Unfold's admin styles
        ],
        'bodyClass': 'unfold-body',  # Apply Unfold's body class
        'filebrowserBrowseUrl': '/ckeditor/browse/',
        'filebrowserUploadUrl': '/ckeditor/upload/',
        'filebrowserImageBrowseUrl': '/ckeditor/browse/?type=Images',
        'filebrowserImageUploadUrl': '/ckeditor/upload/?type=Images',
    }
}
