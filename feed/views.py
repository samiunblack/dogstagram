from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from user.models import UserProfile
from post.models import Post


@login_required
def home(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
    posts = Post.objects.all()    
    return render(request, 'feed/home.html', {'user': user, 'profile': user_profile, 'posts': posts})