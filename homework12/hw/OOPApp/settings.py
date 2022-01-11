import os

from dotenv import find_dotenv, load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'main.db'),
    }
}

INSTALLED_APPS = (
    'data',
)


load_dotenv(find_dotenv())

SECRET_KEY = os.environ['SECRET_KEY']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
