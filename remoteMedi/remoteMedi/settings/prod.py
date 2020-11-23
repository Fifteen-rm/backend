from .base import *
import os

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
DEBUG = True
HOST = os.getenv('DEBUG_HOST')
INSTALLED_APPS += ['django_s3_storage']
S3_BUCKET = "zappa-sv7emz4ut"
STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
AWS_S3_BUCKET_NAME_STATIC = S3_BUCKET
STATIC_URL = "https://%s.s3.amazonaws.com/" % S3_BUCKET

#ALLOWED_HOSTS = ["127.0.0.1", "kauth.kakao.com", "vjbw52tg5f.execute-api.us-east-2.amazonaws.com"]
ALLOWED_HOSTS = ["*"]

if os.getenv("GITHUB_WORKFLOW"):
   DATABASES = {
        'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'github_actions',
           'USER': 'postgres',
           'PASSWORD': 'postgres',
           'HOST': '127.0.0.1',
           'PORT': '5432',
        }
    }
else: # .env
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('DB_NAME'), # dbname
            'USER': os.getenv('MYSQL_ID'), # master username
            'PASSWORD': os.getenv('MYSQL_PW'), # master password
            'HOST': os.getenv('MYSQL_IP'), # Endpoint
            'PORT': os.getenv('MYSQL_PORT')
    }
}
