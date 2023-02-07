import json

import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import CreateUserForm, UserResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserResponseForm
from json import dumps
from django.http import JsonResponse
from collections import Counter


@login_required(login_url='/login')
def home_page(request):
    return render(request, 'home.html')


@login_required(login_url="/login")
def test_page(request):
    latest_response = UserResponse.objects.filter(user=request.user).values().latest("date_time")
    vals = [latest_response[i] for i in latest_response]
    stage_num = vals[2]
    vals = vals[3:8]
    counts = dict(Counter(vals))
    num_yes_no = {key: value for key, value in counts.items() if value > 1}
    num_yes_no = vals.count("Yes")
    print(num_yes_no)
    if num_yes_no > 2:
        messages.success(request, 'You can give Second Test!')
    return render(request, 'test_page.html')


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
    form = UserResponseForm()

    if request.method == 'POST':
        form = UserResponseForm(request.POST)
        first_ques = request.POST.get("first_ques")
        second_ques = request.POST.get("second_ques")
        third_ques = request.POST.get("third_ques")
        fourth_ques = request.POST.get("fourth_ques")
        fifth_ques = request.POST.get("fifth_ques")
        request.user.userresponse_set.create(stage_number=1, first_ques=first_ques, second_ques=second_ques,
                                             third_ques=third_ques, fourth_ques=fourth_ques, fifth_ques=fifth_ques)

        user_response = UserResponse.objects.filter(user=request.user).latest("date_time")

        return render(request, 'test_view.html', {'data': user_response, 'form': form})

    else:
        return render(request, 'test.html', {"form": form})


def analyze_user_response(response, id):
    global df
    test_data = UserResponse.objects.values().get(pk=id)
    test_data_json = dumps(test_data, default=str)
    vals = [test_data[i] for i in test_data]
    stage_num = vals[2]
    vals = vals[3:8]
    if stage_num == 1:
        print("Stage-1")
        df = pd.read_csv('Datasets/Stage-1.csv')
    elif stage_num == 2:
        print("Stage-2")
        df = pd.read_csv('Datasets/Stage-2.csv')
    elif stage_num == 3:
        print("Stage-3")
        df = pd.read_csv('Datasets/Stage-3.csv')

    proc_df = df.loc[:, df.columns != 'Answers']
    proc_df.loc[len(proc_df)] = vals
    dup_df = proc_df[proc_df.duplicated(keep=False)]
    result = df.iloc[dup_df.index[0]]['Answers']
    return render(response, 'analyze_test.html', {'result': result})


@login_required(login_url='/login')
def stage2_test_response(request):
    form = UserResponseForm()

    if request.method == 'POST':
        form = UserResponseForm(request.POST)
        first_ques = request.POST.get("first_ques")
        second_ques = request.POST.get("second_ques")
        third_ques = request.POST.get("third_ques")
        fourth_ques = request.POST.get("fourth_ques")
        fifth_ques = request.POST.get("fifth_ques")
        request.user.userresponse_set.create(stage_number=2, first_ques=first_ques, second_ques=second_ques,
                                             third_ques=third_ques, fourth_ques=fourth_ques, fifth_ques=fifth_ques)

        user_response = UserResponse.objects.filter(user=request.user).latest("date_time")

        return render(request, 'test_view.html', {'data': user_response, 'form': form})

    else:
        return render(request, 'Stage-2_test.html', {"form": form})


@login_required(login_url='/login')
def stage3_test_response(request):
    form = UserResponseForm()

    if request.method == 'POST':
        form = UserResponseForm(request.POST)
        first_ques = request.POST.get("first_ques")
        second_ques = request.POST.get("second_ques")
        third_ques = request.POST.get("third_ques")
        fourth_ques = request.POST.get("fourth_ques")
        fifth_ques = request.POST.get("fifth_ques")
        request.user.userresponse_set.create(stage_number=3, first_ques=first_ques, second_ques=second_ques,
                                             third_ques=third_ques, fourth_ques=fourth_ques, fifth_ques=fifth_ques)

        user_response = UserResponse.objects.filter(user=request.user).latest("date_time")
        return render(request, 'test_view.html', {'data': user_response, 'form': form})
    else:
        return render(request, 'Stage-3_test.html', {"form": form})


@login_required(login_url="/login")
def analyze_user_report(request):
    user_data = UserResponse.objects.filter(user=request.user).values("date_time", "first_ques",
                                                                      "third_ques", 'second_ques', 'fourth_ques',
                                                                      'fifth_ques').order_by("-id")[:10][::1]

    return render(request, 'Analyze/analyze_user.html', {'user_data': user_data})


def get_user_json(request):
    user_data = UserResponse.objects.filter(user=request.user).values("date_time", "first_ques",
                                                                      "third_ques", 'second_ques', 'fourth_ques',
                                                                      'fifth_ques').order_by("-id")[:10][::1]

    user_data = list(user_data)
    user_data_json = json.dumps(user_data, default=str)

    return JsonResponse(user_data_json, safe=False)
