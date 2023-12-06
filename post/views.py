from django.shortcuts import render, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # form.save()
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('home')
        else:
            return render(request, 'post/create_post.html', {'form': form})
    else:
        form = PostForm()

    return render(request, 'post/create_post.html', {'form': form})
    
def show(request):
    pass