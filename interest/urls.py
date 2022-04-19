from django.urls import path
from .views import AddInterest, ListInterest

urlpatterns = [
    path('interest/add_interest', AddInterest.as_view(), name='add_interest'),
    path('interests/list_interest', ListInterest.as_view(), name='list_interest')
]
