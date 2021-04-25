from django.urls import path
from apps.cp.api.api import cp_api_view

urlpatterns = [
    path('api/', cp_api_view, name='api_cp'),
]