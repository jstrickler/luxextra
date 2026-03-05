from .base import *

DEBUG = True

# get common settings from the base settings modulel

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0yymwk1*q=!a9(9+g6jo%05)w_&+!$t3$jc!#_h(l9jb3y(07c'

# When DEBUG is True, Will allow '127.0.0.1', 'LocalHost', and '[::1]'
ALLOWED_HOSTS = []

# add the Django Debug Toolbar
#---------------------------------------------------------------------------
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INSTALLED_APPS += ['debug_toolbar', ]

INTERNAL_IPS = ['127.0.0.1']

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}
#---------------------------------------------------------------------------

# Celery
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"
