""" Initialize Django stuff before any other imports """
import django
import os
from django.conf import settings
from autohub import settings as my_settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autohub.settings')
django.setup()