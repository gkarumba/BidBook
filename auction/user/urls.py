
from django.urls import path, include
from .views import LoginView, RegisterUsersView, UserViewSet,  UsersProfileViewSet, RolesViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('profile', UsersProfileViewSet)
router.register('users', UserViewSet)
router.register('roles', RolesViewSet )

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsersView.as_view(), name="auth-register"),
    path('', include(router.urls)),
    
]

