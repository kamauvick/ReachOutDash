from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ChvForm, PatientForm, EmergencyForm, RoadStatusForm, UpdateChvForm
from .forms import SignupForm
from .models import *


def landing(request):
    title = 'Landing page'
    context = {
        'title': title,
    }

    return render(request, 'landing/index.html', context)


@login_required(login_url='login')
def index(request):
    return render(request, 'main/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='login')
def create_chv(request):
    if request.method == 'POST':
        form = ChvForm(request.POST)
        if form.is_valid():
            chv = form.save(commit=False)
            chv.area = request.user.profile.location
            chv.save()
    else:
        form = ChvForm()
    return render(request, 'main/model_views/add_chv.html', {'form': form})


@login_required(login_url='login')
def new_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
    else:
        form = PatientForm()
    return render(request, 'main/model_views/data_collection_tool.html', {'form': form})


@login_required(login_url='login')
def new_emergency(request):
    if request.method == 'POST':
        form = EmergencyForm(request.POST)
        if form.is_valid():
            emergency = form.save(commit=False)
            emergency.location = request.user.profile.location
            emergency.save()
    else:
        form = EmergencyForm()
    return render(request, 'main/model_views/emergency_report.html', {'form': form})


@login_required(login_url='login')
def access_status(request):
    if request.method == 'POST':
        form = RoadStatusForm(request.POST)
        if form.is_valid():
            road_status = form.save(commit=False)
            road_status.save()
    else:
        form = RoadStatusForm()
    return render(request, 'main/model_views/accesibility_status.html', {'form': form})


def profile(request, username):
    return render(request, 'main/model_views/chv_profile.html')


@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateChvForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('main/model_views/chv_profile.html', user.username)
    else:
        form = UpdateChvForm(instance=request.user.profile)
    return render(request, 'main/model_views/edit_chv_profile.html', {'form': form})
