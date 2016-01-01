"""
Django local settings, changed per environment
"""
try:
    from .settings_base import *
except ImportError:
    pass

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j(buu9@an#0$5&ri*)stjf-gb5#rc8vukg9-j78jaldseg*6di'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True