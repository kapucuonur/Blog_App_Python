from django.conf import settings
from django.http import HttpResponsePermanentRedirect

class ForceHttpInDevelopmentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.DEBUG and request.headers.get('X-Forwarded-Proto') == 'https':
            return HttpResponsePermanentRedirect(request.build_absolute_uri().replace('https://', 'http://'))
        return self.get_response(request)