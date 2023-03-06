from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username "{username}" is already taken.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, f'Email "{email}" is already taken.')
            else:
                form.save()
                messages.success(request, f'Your account has been created! you are now able to log in.')
                return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})