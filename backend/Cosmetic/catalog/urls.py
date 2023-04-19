from django.urls import path

from catalog.api import CreamsAPiView


urlpatterns = [
    path("api/products/", CreamsAPiView.as_view()),
]
