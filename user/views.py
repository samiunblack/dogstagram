from django.shortcuts import render
from .forms import NewUserForm


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
    else:  
        form = NewUserForm()
    return render (request=request, template_name="registration/register.html", context={"register_form":form})