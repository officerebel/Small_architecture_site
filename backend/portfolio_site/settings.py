import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY', default='your-secret-key-here-change-in-production')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=lambda v: [s.strip() for s in v.split(',')])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Wagtail apps
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
    
    # Wagtail API
    'wagtail.api.v2',
    
    # Third party apps
    'modelcluster',
    'taggit',
    'rest_framework',
    'corsheaders',
    
    # Local apps
    'portfolio',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'portfolio_site.urls'

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

import dj_database_url

# Database configuration
DATABASE_URL = config('DATABASE_URL', default='')

if DATABASE_URL:
    # Use DATABASE_URL (Railway or local)
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL)
    }
else:
    # Use individual database settings
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DATABASE_NAME', default='portfolio'),
            'USER': config('DATABASE_USER', default='postgres'),
            'PASSWORD': config('DATABASE_PASSWORD', default='postgres123'),
            'HOST': config('DATABASE_HOST', default='localhost'),
            'PORT': config('DATABASE_PORT', default='5432'),
        }
    }

# Wagtail settings
WAGTAIL_SITE_NAME = "Portfolio Site"
WAGTAIL_ENABLE_UPDATE_CHECK = False

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# CORS settings
FRONTEND_URL = config('FRONTEND_URL', default='http://localhost:9000')
CORS_ALLOWED_ORIGINS = [
    FRONTEND_URL,
    "http://localhost:9000",
    "http://127.0.0.1:9000",
]

# Allow CORS for all origins in development
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    # Temporarily allow all origins for debugging
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOWED_ORIGINS.extend(config('ADDITIONAL_CORS_ORIGINS', default='', cast=lambda v: [s.strip() for s in v.split(',') if s.strip()]))

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}

# Wagtail API settings
WAGTAILAPI_BASE_URL = config('WAGTAILADMIN_BASE_URL', default='http://localhost:8002')
# Static files (CSS, JavaScript, Images)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security settings for production
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# Wagtail settings
WAGTAILADMIN_BASE_URL = config('WAGTAILADMIN_BASE_URL', default='http://localhost:8002')