from django.urls import path
from . import views

urlpatterns = [
    path("create/<int:pk>", views.create_comment, name="create_comment"),
    path("delete/<int:pk>", views.delete, name="delete_comment"),
]
