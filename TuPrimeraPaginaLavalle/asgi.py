<<<<<<< HEAD
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TuPrimeraPaginaLavalle.settings')
=======
"""
ASGI config for TuPrimeraPaginaLavalle project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TuPrimeraPaginaLavalle.settings')

>>>>>>> e4ab1ce1c256aac76b0ac87e71e46064d2c4c12b
application = get_asgi_application()
