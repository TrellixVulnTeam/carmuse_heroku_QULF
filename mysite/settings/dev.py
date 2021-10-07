from .base import *
from django.core.management.utils import get_random_secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-vb7q_xxf5yp==!n9a*h)w6pmtv--@rsul@5h73t_zleqy7+1-b'
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: define the correct hosts in production!
#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = os.getenv("127.0.0.1,localhost", "carmuse-do-o5jq9.ondigitalocean.app").split(",")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
