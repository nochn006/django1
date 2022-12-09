import os

from .djangocore.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ryasik.settings')

application = get_wsgi_application()
