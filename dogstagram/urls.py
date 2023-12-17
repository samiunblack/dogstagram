from django.contrib import admin
from django.urls import path, include
from user.views import register_request, profile, delete_request
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("feed.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/register/", register_request, name="register"),
    path("accounts/<str:username>/", profile, name="profile"),
    path("accounts/delete/<str:username>/", delete_request, name="delete_profile"),
    path("", include("post.urls")),
    path("comment/", include("comment.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)