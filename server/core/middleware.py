from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

class DisableCSRFMiddleware(MiddlewareMixin):
    """
    Middleware to disable CSRF for API endpoints
    This is a GLOBAL setting that applies to all /api/ paths
    """
    def process_request(self, request):
        if request.path.startswith('/api/'):
            setattr(request, '_dont_enforce_csrf_checks', True)


class GlobalAuthorizationMiddleware(MiddlewareMixin):
    """
    MIDDLEWARE APPROACH: Global authorization rules
    
    Use this for BROAD rules that apply to many endpoints:
    - Checking if user is authenticated for all /api/ endpoints
    - Blocking access to entire URL patterns based on roles
    - Enforcing system-wide access policies
    
    This runs BEFORE views, so it's efficient for blanket rules.
    """
    
    def process_request(self, request):
        # Example 1: All /api/pages/ endpoints require authentication
        if request.path.startswith('/api/pages/'):
            if not request.user.is_authenticated:
                return JsonResponse(
                    {'error': 'Authentication required'}, 
                    status=401
                )
        
        # Example 2: All /api/admin/ URLs require superuser (global rule)
        # if request.path.startswith('/api/admin/'):
        #     if not request.user.is_superuser:
        #         return JsonResponse(
        #             {'error': 'Admin access required'}, 
        #             status=403
        #         )
        
        # Example 3: Block all POST/DELETE for read-only users
        # if hasattr(request.user, 'is_readonly') and request.user.is_readonly:
        #     if request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
        #         return JsonResponse(
        #             {'error': 'Read-only user cannot modify data'}, 
        #             status=403
        #         )
        
        return None  # Continue to view if no rules triggered
