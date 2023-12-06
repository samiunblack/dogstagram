from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .models import Post

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
            form.save_m2m() 
            return redirect('show_post')
        else:
            return render(request, 'post/create_post.html', {'form': form})
    else:
        form = PostForm()

    return render(request, 'post/create_post.html', {'form': form})
 
@login_required  
def show(request):
    posts = Post.objects.all()
    return render(request, "post/show_posts.html", {"posts": posts, "user": request.user})

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.user == post.owner:
        post.delete()
    return redirect("show_post")


def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # form.save()
            post = form.save(commit=False)
            post.save()
            form.save_m2m() 
            return redirect('show_post')
        else:
            return render(request, 'post/create_post.html', {'form': form})

    return render(request, 'post/create_post.html', {'form': form})