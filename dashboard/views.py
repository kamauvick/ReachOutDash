from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import SignupForm
from .requests import get_chvs


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    chvs = get_chvs()
    title = 'Reach-Out Dashboard'
    context = {
        'title': title,
        'chvs': chvs,
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
