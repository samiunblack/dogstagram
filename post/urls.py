from django.urls import path
from .views import show, delete, edit, CreatePost

urlpatterns = [
    path("create/", CreatePost.as_view(), name="create_post"),
    path("show/", show, name="show_post"),
    path("delete/<int:pk>", delete, name="delete_post"),
    path("edit/<int:pk>", edit, name="edit_post"),
]
