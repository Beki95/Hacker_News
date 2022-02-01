from django.urls import path

from apps.users.views import register, profile
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),
    path('profile/', profile, name='profile')
]
