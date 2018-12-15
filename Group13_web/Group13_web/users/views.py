from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.gender= form.cleaned_data.get('gender')
            user.profile.hobbies= form.cleaned_data.get('hobbies')
            user.save()
            messages.success(request, f'Account created for {username}! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render (request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
