from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def root_view(request):
    """Simple root endpoint for testing"""
    return JsonResponse({
        'message': 'Portfolio Site API is running',
        'endpoints': {
            'health': '/health/',
            'admin': '/admin/',
            'cms': '/cms/',
            'api': '/api/',
            'wagtail_api': '/api/v2/pages/'
        }
    })