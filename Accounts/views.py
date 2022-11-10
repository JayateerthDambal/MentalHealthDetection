from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home_page(request):
    return render(request, 'home.html')


def signup_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            form.save()
            return redirect('/login')

    context = {'form': form}

    return render(request, 'Accounts/sign_up.html', context)


def login_page(response):
    if response.method == 'POST':
        username = response.POST.get('username')
        password = response.POST.get('password')
        user = authenticate(response, username=username, password=password)
        if user is not None:
            login(response, user=user)
            return redirect('/', {'user_name': username})

        else:
            messages.info(response, 'Username/Password Incorrect')

    return render(response, 'Accounts/login.html')


@login_required(login_url='/login')
def logout_page(request):
    logout(request)
    return redirect('/login')