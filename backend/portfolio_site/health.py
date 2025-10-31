from django.http import JsonResponse
from django.db import connection

def health_check(request):
    """Simple health check endpoint"""
    import os
    from django.conf import settings
    
    response_data = {
        'status': 'healthy',
        'django': 'working',
        'environment': os.environ.get('RAILWAY_ENVIRONMENT', 'local'),
        'debug': settings.DEBUG,
        'allowed_hosts': settings.ALLOWED_HOSTS,
    }
    
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        response_data['database'] = 'connected'
    except Exception as e:
        response_data['database'] = f'error: {str(e)}'
        response_data['status'] = 'unhealthy'
        return JsonResponse(response_data, status=500)
    
    return JsonResponse(response_data)