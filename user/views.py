from django.shortcuts import render, redirect
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


def profile(request, username):
    try:
        user = User.objects.get(username=username)
        return render(request, 'user/profile.html', {"user": user, "admin": request.user})
    except User.DoesNotExist:
        return render(request, 'user/profile.html', {"user": None, "admin": None})