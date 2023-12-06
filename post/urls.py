from django.urls import path
from .views import create, show

urlpatterns = [
    path("create/", create),
    path("show/", show),
]
