from django.urls import path
from . import views

urlpatterns = [
    path('api/login/', views.login_view, name='login'),
    path('api/logout/', views.logout_view, name='logout'),
    path('api/check-auth/', views.check_auth, name='check_auth'),
    path('api/pages/admin/', views.admin_page, name='admin_page'),
    path('api/pages/manager/', views.manager_page, name='manager_page'),
    path('api/pages/operator/', views.operator_page, name='operator_page'),
]
