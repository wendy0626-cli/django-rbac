"""
WSGI config for djangoProject1 project.

It exposes the WSGI callable as a module-level letiable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject1.settings")

application = get_wsgi_application()
