from .base import *

DEBUG = False


# SECURITY WARNING: keep the secret key used in production secret! Read it from a file or from the environment
SECRET_KEY = '3)@@zw6dywt$8-gj-^o3l9psnhreq5+d(f%9_5&9m&qozti+5o'

# specify which domain names Django can serve (IOW the server the site is running on); this prevents HTTP host header
# attacks
ALLOWED_HOSTS = []  # put the site's hostnames here as  www.spam.com and spam.com

MESSAGE_LEVEL = 20  # do not show debug messages