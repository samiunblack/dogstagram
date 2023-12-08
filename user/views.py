from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import NewUserForm
from django.contrib.auth.models import User

def register_request(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            
            if user != None:
                login(request, user)
            
            return redirect("home")
    return render (request=request, template_name="registration/register.html", context={"register_form":form})

def delete_request(request, username):
    user = get_object_or_404(User, username=username)
    
    if user == request.user:
        user.delete()
    
    return redirect("home")


def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user/profile.html', {"user": user, "admin": request.user})