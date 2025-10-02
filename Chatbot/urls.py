from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='homepage'),
    path('get-response/', ai_response, name='ai_response' ),
]

