"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
import sys

# Add your project root directory to the Python path
sys.path.append('/home/ubuntu/career_app')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()