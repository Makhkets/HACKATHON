import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from datetime import timedelta


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG") == "TRUE"

ALLOWED_HOSTS = ['web', '*']

# Application definition

INSTALLED_APPS = [
    'django_extensions',
    'django.contrib.admin',
    'django_quill',
    'import_export',
    'ordered_model',
    'smuggler',
    'django_editorjs',
    'django_editorjs_fields',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'celery',
    'treebeard',
    'djmoney',
    'storages',
    'corsheaders',
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt.token_blacklist',
    'api.v1.users',
    'api.v1.files',
    'api.v1.images',
    'api.v1.billing',
    'api.v1.referals',
    'api.v1.texts',
    'silk',
    'oauth2_provider',
    'social_django',
    'drf_social_oauth2',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'silk.middleware.SilkyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
]



SESSION_COOKIE_SAMESITE = None
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL = True

SILKY_PYTHON_PROFILER = True
SILKY_PYTHON_PROFILER_BINARY = True
if DEBUG:
    SILKY_INTERCEPT_PERCENT = 100
else:
    SILKY_INTERCEPT_PERCENT = 5
SILKY_AUTHENTICATION = True  # User must login
SILKY_AUTHORISATION = True  # User must have permissions
SILKY_META = True
SILKY_ANALYZE_QUERIES = True
SILKY_MAX_RECORDED_REQUESTS = 10**4
SILKY_MAX_RECORDED_REQUESTS_CHECK_PERCENT = 10

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    '172.18.0.8'
    # ...
]

ROOT_URLCONF = 'Trumedia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'Trumedia.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
CONN_MAX_AGE = 60*5
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT"),
    }
}

AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
    # 'api.v1.users.custom-auth-backends.AppleIdMobile.AppleIdMobile',
    'drf_social_oauth2.backends.DjangoOAuth2',
    # 'social_core.backends.apple.AppleIdAuth',
)

SOCIAL_AUTH_APPLE_ID_CLIENT = 'com.beautytwins.solutions'
SOCIAL_AUTH_APPLE_ID_TEAM = 'TPV6754L84'
SOCIAL_AUTH_APPLE_ID_KEY = '4VY9ZY3623'
SOCIAL_AUTH_APPLE_ID_SECRET = """
-----BEGIN PRIVATE KEY-----
MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgEFeuEWbuWyHeRhqN
GqZFo6ICJ07cEhguf7MnBeWF6sGgCgYIKoZIzj0DAQehRANCAAToYLHWDTdlpE5T
TPxyM5d1QUVX3kORXv6HxmA2/umpxa2bm81CQ6Y9ZrEic5KDklUVFzQnVbids6T+
zAs0mqtA
-----END PRIVATE KEY-----"""
SOCIAL_AUTH_APPLE_ID_SCOPE = ['email', 'name']
SOCIAL_AUTH_APPLE_ID_EMAIL_AS_USERNAME = False   # If you want to use email as username

SOCIAL_AUTH_APPLE_ID_MOBILE_CLIENT = 'com.beautytwins.solutions1'
SOCIAL_AUTH_APPLE_ID_MOBILE_TEAM = SOCIAL_AUTH_APPLE_ID_TEAM
SOCIAL_AUTH_APPLE_ID_MOBILE_KEY = SOCIAL_AUTH_APPLE_ID_KEY
SOCIAL_AUTH_APPLE_ID_MOBILE_SECRET = SOCIAL_AUTH_APPLE_ID_SECRET
SOCIAL_AUTH_APPLE_ID_MOBILE_SCOPE = SOCIAL_AUTH_APPLE_ID_SCOPE
SOCIAL_AUTH_APPLE_ID_MOBILE_EMAIL_AS_USERNAME = SOCIAL_AUTH_APPLE_ID_EMAIL_AS_USERNAME

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

OAUTH2_PROVIDER = {
    'ACCESS_TOKEN_EXPIRE_SECONDS': 60 * 60 * 10,  # 10 hours
    'REFRESH_TOKEN_EXPIRE_SECONDS': 60 * 60 * 24 * 30 * 12,  # 1 year
    'OAUTH_DELETE_EXPIRED': True,
    'SCOPES': {
        "read": 'Read scope',
        "write": 'Write scope',
        'groups': 'Access to your groups'
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'drf_social_oauth2.authentication.SocialAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
DATA_UPLOAD_MAX_MEMORY_SIZE = 15242880

RABBIT_USER = os.environ.get("RABBIT_USER")
RABBIT_PASSWORD = os.environ.get("RABBIT_PASSWORD")
BROKER_POOL_LIMIT = 10
CELERYD_FORCE_EXECV = True
CELERY_TASK_RESULT_EXPIRES = 3600
CELERYD_POOL_RESTARTS = True
CELERY_ACKS_LATE = False
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_RESULT_BACKEND = "rpc://"
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
# CELERY_RESULT_BACKEND = f'pyamqp://{os.environ.get("RABBITMQ_DEFAULT_USER")}:{os.environ.get("RABBITMQ_DEFAULT_PASS")}@rabbit:5672'

AUTH_USER_MODEL = 'users.User'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")
FRONTEND_URL = os.environ.get("FRONTEND_URL")
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("GMAIL_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = 'default from email'

USE_S3 = os.getenv('USE_S3') == 'TRUE'

if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    # AWS_DEFAULT_ACL = None
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # s3 static settings
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'Trumedia.storage_backends.StaticStorage'
    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'Trumedia.storage_backends.PublicMediaStorage'
else:
    STATIC_URL = '/backend_static/'
    STATIC_ROOT = './static/'
    MEDIA_URL = '/backend_media/'
    MEDIA_ROOT = './media/'


# ---------------- Local Settings ---------------------------------------
# Put your local settings in Trumedia directory to override this settings
# File name should be local_settings.py
try:
    from .local_settings import *
except ImportError:
    print('No Local Settings Found')

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
      'simple': {
            'format': 'velname)s %(message)s'
        },
  },
  'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'logstash': {
            'level': 'INFO',
            'class': 'logstash.TCPLogstashHandler',
            'host': 'logstash',
            'port': 5000,
            'version': 1,
            'message_type': 'django',
            'fqdn': False,
            'tags': ['django'],
        }
  },
  'loggers': {
        'django.request': {
            'handlers': ['logstash'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.server': {
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'handlers': ['console', 'logstash'],
            'propagate': True,
        },
        'django': {
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'handlers': ['console', 'logstash'],
            'propagate': True,
        },
        'celery': {
            'handlers': ['console', 'logstash'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    }
}