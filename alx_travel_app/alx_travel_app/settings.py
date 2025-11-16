from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

# env setup
env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, "change-me"),
    ALLOWED_HOSTS=(list, ["127.0.0.1", "localhost"]),
    CORS_ALLOW_ALL_ORIGINS=(bool, True),
)

env_file = BASE_DIR / ".env"
if not env_file.exists():
    env_file = BASE_DIR / "alx_travel_app" / ".env"

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # third-party
    "rest_framework",
    "corsheaders",
    "drf_yasg",

    # local
    "alx_travel_app.alx_travel_app.listings"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",

    # CORS must be high in the list, before CommonMiddleware
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ROOT_URLCONF = "alx_travel_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI_APPLICATION = "alx_travel_app.wsgi.application"

ROOT_URLCONF = "alx_travel_app.alx_travel_app.urls"
WSGI_APPLICATION = "alx_travel_app.alx_travel_app.wsgi.application"
ASGI_APPLICATION = "alx_travel_app.alx_travel_app.asgi.application"

# Database (MySQL via env)
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": env("MYSQL_DATABASE"),
#         "USER": env("MYSQL_USER"),
#         "PASSWORD": env("MYSQL_PASSWORD"),
#         "HOST": env("MYSQL_HOST"),
#         "PORT": env("MYSQL_PORT", default="3306"),
#         "OPTIONS": {"init_command": "SET sql_mode='STRICT_ALL_TABLES'"},
#     }
# }

# Database (PostgreSQL via env)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", default="alxtravel"),
        "USER": env("POSTGRES_USER", default="alxuser"),
        "PASSWORD": env("POSTGRES_PASSWORD", default="alxpass"),
        "HOST": env("POSTGRES_HOST", default="localhost"),
        "PORT": env("POSTGRES_PORT", default="5433"),
    }
}


# If you chose PyMySQL instead of mysqlclient, uncomment below:
# import pymysql
# pymysql.install_as_MySQLdb()

# DRF minimal config
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser"],
}

# Static
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# CORS
CORS_ALLOW_ALL_ORIGINS = env("CORS_ALLOW_ALL_ORIGINS")  # True by default in env block

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

