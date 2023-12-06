from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from post.models import Post
from .models import Comment

# Create your views here.
def create(request, pk):
    form = CommentForm()
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
        
        return redirect("show_post")
    
    return render(request, 'comment/create_comment.html', {"form": form})

def delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    
    if request.user == comment.user:
        comment.delete()
    
    return redirect("show_post")


def edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    form = CommentForm(instance=comment)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        comment = form.save(commit=False)
        comment.save()
        
        return redirect("show_post")
    
    return render(request, 'comment/create_comment.html', {"form": form})