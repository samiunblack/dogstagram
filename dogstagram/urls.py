from django.contrib import admin
from django.urls import path, include
from .views import home
from user.views import register_request, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", register_request, name="register"),
    path("accounts/<str:username>/", profile, name="profile"),
    path("post/", include("post.urls"))
]
