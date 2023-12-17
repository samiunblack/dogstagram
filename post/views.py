from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .models import Post
import requests
import os
from .predict import predictWhat
from dogstagram.settings import imgbb_client_id
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage


def delete_local_image(image_path):
    try:
        os.remove(image_path)
        print(f"Deleted local image at: {image_path}")
    except Exception as e:
        print(f"Error deleting local image: {e}")


def upload_image_to_imgbb(api_key, image_path):
    endpoint = "https://api.imgbb.com/1/upload"

    with open(image_path, "rb") as file:
        files = {"image": file}
        params = {"key": api_key}

        response = requests.post(endpoint, files=files, params=params)
        result = response.json()

        if response.status_code == 200:
            # Successful upload
            return result["data"]["url"]
        else:
            # Print error message or handle the error as needed
            print("Error:", result["error"]["message"])
            return None


# Example usage in a Django view
def upload_image(request):
    
    image_file = request.FILES['image']
    fs = FileSystemStorage(base_url='/media/temp/', location="media/temp/")
    filename = fs.save(image_file.name, image_file)
    
    result = predictWhat('media/temp/' + filename)
    
    if result:
        imgbb_api_key = imgbb_client_id
        uploaded_image_url = upload_image_to_imgbb(imgbb_api_key, 'media/temp/' + filename)
        delete_local_image('media/temp/' + filename)
        return uploaded_image_url, filename
    else:
        delete_local_image('media/temp/' + filename)
        return None, filename



@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            url, filename = upload_image(request)
            if url is not None:
                post = form.save(commit=False)
                post.owner = request.user
                post.img_url = url
                post.save()
                form.save_m2m() 
                delete_local_image('media/temp/' + filename)
            else:
                return redirect('profile', username=request.user.username)
            
            return redirect('profile', username=request.user.username)
        else:
            return render(request, 'post/create_post.html', {'form': form})
    else:
        form = PostForm()

    return render(request, 'post/create_post.html', {'form': form})



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