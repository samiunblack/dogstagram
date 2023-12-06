from django.contrib import admin
from django.urls import path, include
from user.views import register_request, profile, delete_request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("feed.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", register_request, name="register"),
    path("accounts/<str:username>/", profile, name="profile"),
    path("accounts/delete/<str:username>/", delete_request, name="delete_profile"),
    path("post/", include("post.urls")),
    path("comment/", include("comment.urls")),
]
