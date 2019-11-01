from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import SignupForm, UpdateProfileForm
from .models import User
from .requests import get_chvs, get_patients, get_emergencies, get_locations


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    chvs = get_chvs()
    patients = get_patients()
    emergencies = get_emergencies()
    locations = get_locations()
    title = 'Reach-Out Dashboard'
    context = {
        'title': title,
        'chvs': chvs,
        'patients': patients,
        'emergencies': emergencies,
        'locations': locations,
    }
    return render(request, 'dash/dash.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='login')
def profile(request, username):
    return render(request, 'dash/profile.html')


def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'dash/edit_profile.html', {'form': form})


@login_required(login_url='login')
def chvs(request):
    chvs = get_chvs()
    title = 'Reach-Out Dashboard'
    context = {
        'title': title,
        'chvs': chvs,
        'patients': patients,
        'emergencies': emergencies,
        'locations': locations,
    }
    return render(request, 'dash/main/chvs.html', context)


@login_required(login_url='login')
def patients(request):
    patients = get_patients()
    title = 'Reach-Out Dashboard'
    context = {
        'title': title,
        'chvs': chvs,
        'patients': patients,
        'emergencies': emergencies,
        'locations': locations,
    }
    return render(request, 'dash/main/patients.html', context)


@login_required(login_url='login')
def emergencies(request):
    emergencies = get_emergencies()
    title = 'Reach-Out Dashboard'
    context = {
        'title': title,
        'chvs': chvs,
        'patients': patients,
        'emergencies': emergencies,
        'locations': locations,
    }
    return render(request, 'dash/main/emergencies.html', context)


@login_required(login_url='login')
def locations(request):
    locations = get_locations()
    title = 'Reach-Out Dashboard'
    context = {
        'title': title,
        'chvs': chvs,
        'patients': patients,
        'emergencies': emergencies,
        'locations': locations,
    }
    return render(request, 'dash/main/locations.html', context)


@login_required(login_url='login')
def about(request):
    chvs = get_chvs()
    patients = get_patients()
    emergencies = get_emergencies()
    locations = get_locations()
    title = 'Reach-Out Dashboard'
    context = {
        'title': title,
        'chvs': chvs,
        'patients': patients,
        'emergencies': emergencies,
        'locations': locations,
    }
    return render(request, 'dash/main/about.html', context)
