from django.urls import path
from . import views

urlpatterns = [
    path("create/<int:pk>", views.create, name="create_comment"),
    path("delete/<int:pk>", views.delete, name="delete_comment"),
    path("edit/<int:pk>", views.edit, name="edit_comment"),
]
