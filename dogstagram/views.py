from django.shortcuts import render


def home(request):
    user = request.user
    return render(request, 'global/home.html', {'user': user})