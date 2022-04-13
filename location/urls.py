from django.urls import path
from .views import LocationCreateView

urlpatterns = [
    path('addlocation/', LocationCreateView.as_view(), name='save_location'),
]