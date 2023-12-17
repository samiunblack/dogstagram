from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .models import Post
import requests
import os
from dogstagram.settings import imgur_client_id
from django.views.generic import CreateView
from django.urls import reverse_lazy


def upload_image_to_imgur(image_path, client_id):
    # Imgur API endpoint
    url = "https://api.imgur.com/3/image"

    # Set up headers with authorization
    headers = {"Authorization": f"Client-ID {client_id}"}

    # Open the image file and send a POST request to Imgur
    with open(image_path, "rb") as image_file:
        files = {"image": image_file}
        data = {"type": "url", "hidden": "true"}
        response = requests.post(url, headers=headers, files=files, data=data)

    # Parse the response and get the image URL
    if response.status_code == 200:
        return response.json()["data"]["link"]
    else:
        return None


# Example usage in a Django view
def upload_image(request):
    if request.method == 'POST':
        # Assume the uploaded file is in request.FILES['image']
        uploaded_image = request.FILES['temp']

        # Save the uploaded image to a temporary file
        with open('temp_image.jpg', 'wb') as temp_file:
            for chunk in uploaded_image.chunks():
                temp_file.write(chunk)

        # Replace 'your_imgur_client_id' with your actual Imgur API client ID
        print(imgur_client_id)
        imgur_url = upload_image_to_imgur('temp_image.jpg', imgur_client_id)

        # Save the Imgur URL to your database
        # ...

        # Cleanup: Delete the temporary file
        os.remove('temp_image.jpg')

        # Continue with the rest of your view logic
        # ...



# Create your views here.
# @login_required
# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             # post = form.save(commit=False)
#             # post.owner = request.user
#             # post.save()
#             # form.save_m2m() 
#             return redirect('profile', username=request.user.username)
#         else:
#             return render(request, 'post/create_post.html', {'form': form})
#     else:
#         form = PostForm()

#     return render(request, 'post/create_post.html', {'form': form})

class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/create_post.html'
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
 
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