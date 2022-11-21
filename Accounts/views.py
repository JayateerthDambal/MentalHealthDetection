from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import CreateUserForm, UserResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def record_response(request):
    form = UserResponse()

    if request.method == 'POST':
        form = UserResponse(request.POST)
        age = request.POST.get('age')
        course = request.POST.get('course')
        anxiety = request.POST.get('anxiety')
        depression = request.POST.get('depression')
        panic_attack = request.POST.get('panic_attack')
        marital_status = request.POST.get('marital_status')
        smoking = request.POST.get('smoking')
        drinking = request.POST.get('drinking')
        specialist = request.POST.get('specialist')
        drugs = request.POST.get('drugs')
        request.user.userresponse_set.create(age=age, course=course, anxiety=anxiety, depression=depression,
                                             panic_attack=panic_attack, marital_status=marital_status,
                                             smoking=smoking, drinking=drinking, seeked_specialist=specialist,
                                             drugs=drugs)

        user_response = UserResponse.objects.filter(user=request.user).all()

        return render(request, 'test_view.html', {'data': user_response})

    else:
        return render(request, 'test.html')
