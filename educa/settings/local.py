from .base import *

DEBUG = True

SECRET_KEY = "ybx5d+youn7^%kho86%+%fenz8!&=jpwe%z7_@ygj7l9nskk*l"

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
