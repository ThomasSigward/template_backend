from .base import *

DEBUG = False

if SECRET_KEY.startswith("django-insecure-"):
    raise RuntimeError("A secure DJANGO_SECRET_KEY is required.")

if not ALLOWED_HOSTS:
    raise RuntimeError("DJANGO_ALLOWED_HOSTS must be configured.")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True