import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "python_m5_a1_ai_augmented.settings")
application = get_wsgi_application()
