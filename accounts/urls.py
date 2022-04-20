from django.urls import path
from .views import SignUpAPIView, LoginAPIView, UserProfileView, UserProfileCreateView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('account/signup/', SignUpAPIView.as_view(), name='signup'),
    path('account/login/', LoginAPIView.as_view(), name='sign_in'),
    path('account/refreshToken/', TokenRefreshView.as_view(), name='refresh_token'),
    path('account/profile/<str:username>', UserProfileView.as_view(), name='view_profile'),
    path('account/profile/<str:username>/create', UserProfileCreateView.as_view(), name='create_profile')
]