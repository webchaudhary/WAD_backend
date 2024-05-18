from django.urls import path
from .views import kenya_dashboard

urlpatterns = [
    path('', kenya_dashboard, name='kenya_dashboard'),
]
