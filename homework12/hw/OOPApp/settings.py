import os


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

SECRET_KEY = '4e&6aw+(5&cg^_!05r(&7_#dghg_pdgopq(yk)xa^bog7j)^*j'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
