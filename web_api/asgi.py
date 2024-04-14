"""
ASGI config for web_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

import uvicorn

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_api.settings")

application = get_asgi_application()


if __name__ == "__main__":
    uvicorn.run("web_api.asgi:application", reload=True)