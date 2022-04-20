from django.urls import path
from .views import UserLocationCreateView

urlpatterns = [
    path('addlocation/', UserLocationCreateView.as_view(), name='save_location'),
]