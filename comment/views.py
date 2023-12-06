from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from post.models import Post
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Comment

# Create your views here.
def create(request, pk):
    form = CommentForm()
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        
        return redirect("show_post")
    
    return render(request, 'comment/create_comment.html', {"form": form})

@require_POST
def create_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_text = request.POST.get('comment')

    # Save the comment
    comment = Comment.objects.create(
        post=post,
        user=request.user,
        text=comment_text
    )
    comment.save()
    return redirect("home")


def delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    
    if request.user == comment.user:
        comment.delete()
    
    return redirect("home")
