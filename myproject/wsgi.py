"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import threading
import time
import requests

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = get_wsgi_application()

def ping_self():
    """
    Function to ping the app's own URL to keep it alive on Render.com
    Render free tier sleeps after 15 minutes of inactivity.
    """
    app_url = os.getenv("APP_URL")
    if not app_url:
        print("APP_URL not set. Self-ping disabled.")
        return

    print(f"Starting self-ping for {app_url}")
    while True:
        try:
            # Wait 14 minutes (840 seconds)
            time.sleep(840)
            print(f"Pinging {app_url}/ping...")
            response = requests.get(f"{app_url}/ping")
            print(f"Self-ping response: {response.status_code}")
        except Exception as e:
            print(f"Self-ping error: {e}")

# Start the self-ping thread
threading.Thread(target=ping_self, daemon=True).start()
