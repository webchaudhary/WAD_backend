from django.urls import path
from .views import kenya_dashboard
from .views import kenya_dashboard, get_json_data, get_view_json_data

urlpatterns = [
    path('', kenya_dashboard, name='kenya_dashboard'),
    path('data/<str:filename>/', get_json_data, name='get_json_data'),
    path('featureData/<str:filename>/', get_view_json_data, name='get_view_json_data'),
]

