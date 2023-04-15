from django.urls import path
from rest_framework import routers

from catalog.api import *


urlpatterns = [
    path('api/products/', CreamsAPiView.as_view())
]