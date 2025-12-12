"""
Django settings for student_portal project.

This file contains all configuration settings for the Django project.
It includes installed apps, middleware, database setup, authentication,
static files, templates, and API configurations.
"""

from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent


# -----------------------------
# Security & Debug Settings
# -----------------------------

# Secret key for cryptographic signing (do NOT expose in production)
SECRET_KEY = 'django-insecure-nryot@3p!(z8sjmi2sjhqe3w(*=2^c+^)2l(ownfk$ex+hhhk='

# Debug mode (should be False in production)
DEBUG = True

# Hosts allowed to access the app
ALLOWED_HOSTS = []


# -----------------------------
# Installed Applications
# -----------------------------

INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # REST Framework for building APIs
    'rest_framework',

    # Djoser for user authentication endpoints
    'djoser',

    # Token authentication support
    'rest_framework.authtoken',

    # SimpleJWT for JWT-based authentication
    'rest_framework_simplejwt',

    # Custom app containing service request models & APIs
    'requestsapp',
]


# -----------------------------
# Middleware Configuration
# -----------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# -----------------------------
# URL & Template Settings
# -----------------------------

# Main URL configuration file
ROOT_URLCONF = 'student_portal.urls'

# Template configuration for rendering HTML pages (admin, etc.)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Custom template directories (empty for now)
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI (web server gateway) configuration
WSGI_APPLICATION = 'student_portal.wsgi.application'


# -----------------------------
# Database Configuration
# -----------------------------

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Local SQLite DB
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# -----------------------------
# REST Framework Settings
# -----------------------------

# Global API authentication & permission rules
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # Use JWT authentication for all API views
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # Require login for all API endpoints
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# JWT token header settings
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
}

# Djoser configuration (login using username)
DJOSER = {
    'LOGIN_FIELD': 'username',
}


# -----------------------------
# Password Validation
# -----------------------------

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# -----------------------------
# Localization & Time Settings
# -----------------------------

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# -----------------------------
# Static Files (CSS, Images, JS)
# -----------------------------

STATIC_URL = 'static/'


# Default field type for primary keys
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'