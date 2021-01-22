from .base import *

DEBUG = False

ADMINS = (("Furkalo S", "furkalokbu@gmail.com"),)

ALLOWED_HOSTS = ["educaproject.com", "www.educaproject.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "educa_dev",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
