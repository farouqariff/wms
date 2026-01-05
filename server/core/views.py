from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """Handle user login"""
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response(
            {'error': 'Username and password are required'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        
        # Get user permissions and groups
        permissions = list(user.user_permissions.values_list('codename', flat=True))
        groups = list(user.groups.values_list('name', flat=True))
        
        return Response({
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'username': user.username,
                'is_superuser': user.is_superuser,
                'groups': groups,
                'permissions': permissions,
            }
        }, status=status.HTTP_200_OK)
    else:
        return Response(
            {'error': 'Invalid credentials'}, 
            status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """Handle user logout"""
    logout(request)
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_auth(request):
    """Check if user is authenticated and return user info"""
    user = request.user
    permissions = list(user.user_permissions.values_list('codename', flat=True))
    groups = list(user.groups.values_list('name', flat=True))
    
    return Response({
        'user': {
            'id': user.id,
            'username': user.username,
            'is_superuser': user.is_superuser,
            'groups': groups,
            'permissions': permissions,
        }
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_page(request):
    """
    VIEW APPROACH: Specific authorization for this endpoint
    
    Use views for FINE-GRAINED rules specific to this resource:
    - Checking specific permissions for this exact page
    - Business logic (e.g., "can user edit THIS specific item?")
    - Resource-level authorization
    
    This is MORE FLEXIBLE than middleware because you can:
    - Check complex conditions
    - Access database models
    - Apply different rules per endpoint
    """
    # Specific check: Only superusers can access admin page
    if not request.user.is_superuser:
        return Response(
            {'error': 'You do not have permission to view this page'}, 
            status=status.HTTP_403_FORBIDDEN
        )
    
    return Response({
        'message': 'Only Admin can see this page',
        'page': 'admin'
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def manager_page(request):
    """
    VIEW APPROACH: Specific permission check
    This checks a SPECIFIC permission for THIS endpoint only
    """
    # Specific check: Requires view_manager_page permission OR superuser
    if not (request.user.is_superuser or request.user.has_perm('core.view_manager_page')):
        return Response(
            {'error': 'You do not have permission to view this page'}, 
            status=status.HTTP_403_FORBIDDEN
        )
    
    return Response({
        'message': 'Only Manager can see this page',
        'page': 'manager'
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def operator_page(request):
    """
    VIEW APPROACH: Specific permission check
    This checks a SPECIFIC permission for THIS endpoint only
    """
    # Specific check: Requires view_operator_page permission OR superuser
    if not (request.user.is_superuser or request.user.has_perm('core.view_operator_page')):
        return Response(
            {'error': 'You do not have permission to view this page'}, 
            status=status.HTTP_403_FORBIDDEN
        )
    
    return Response({
        'message': 'Only Operator can see this page',
        'page': 'operator'
    }, status=status.HTTP_200_OK)
