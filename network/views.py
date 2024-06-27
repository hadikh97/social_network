from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile


def home(request):
    return render(request, 'network/templates/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'network/signup.html', {'form': form})


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get_or_create(user=user)[0]
    return render(request, 'network/profile.html', {'user': user, 'profile': profile})
