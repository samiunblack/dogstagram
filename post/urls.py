from django.urls import path
from .views import create_post, show, delete, edit, CreatePost

urlpatterns = [
    path("create/", create_post, name="create_post"),
    path("show/", show, name="show_post"),
    path("delete/<int:pk>", delete, name="delete_post"),
    path("edit/<int:pk>", edit, name="edit_post"),
]
