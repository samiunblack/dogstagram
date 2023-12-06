from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from user.models import UserProfile

@login_required
def home(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'feed/home.html', {'user': user, 'profile': user_profile})