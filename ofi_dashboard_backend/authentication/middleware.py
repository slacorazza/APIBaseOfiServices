from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from rest_framework.authtoken.models import Token

class CheckAPITokenMiddleware(MiddlewareMixin):
    """
    Middleware to check authentication for API calls.

    This middleware ensures that all API requests are authenticated by checking for a valid token.
    """
    def process_request(self, request):
        if request.path.startswith('/api/'):
            token_key = request.META.get('HTTP_AUTHORIZATION')
            if token_key:
                try:
                    token_key = token_key.split(' ')[1]
                    token = Token.objects.get(key=token_key)
                    request.user = token.user
                except (Token.DoesNotExist, IndexError):
                    return JsonResponse({'error': 'Invalid token'}, status=401)
            else:
                return JsonResponse({'error': 'Token required'}, status=401)