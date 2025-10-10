import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'clave-secreta'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'chat',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'mongochat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'chat' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [],
        },
    },
]

WSGI_APPLICATION = 'mongochat.wsgi.application'

STATIC_URL = '/static/'

# === MongoDB Config ===
MONGO_URI = "mongodb://localhost:27017"
MONGO_DB = "chatbot_db"

# === VertexAI Config ===
PROJECT_ID = "stone-poetry-473315-a9"
LOCATION = "us-central1"

# Credenciales de Google (ya configuradas en tu sistema)
GOOGLE_APPLICATION_CREDENTIALS = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
