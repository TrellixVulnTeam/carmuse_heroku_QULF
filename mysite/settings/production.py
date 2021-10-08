from .base import *
from django.core.management.utils import get_random_secret_key

#DEBUG = True # int(os.environ.get("DEBUG", default=1))
DEBUG = os.getenv("DEBUG", "False") == "True"

#SECRET_KEY = 'django-insecure-wt2^elcpvn+a-aa7exnt92ak#l%yozhx+!el^^g1o&z246vyyb'
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = os.getenv["*"]
# try:
#     from .local import *
# except ImportError:
#     pass

from .base import *