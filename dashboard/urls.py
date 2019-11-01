from django.urls import path, include

from .views import dashboard, signup, chvs, patients, emergencies, locations, about, edit_profile, profile

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('signup/', signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('chvs', chvs, name='chvs'),
    path('patients', patients, name='patients'),
    path('emergencies', emergencies, name='emergencies'),
    path('locations', locations, name='locations'),
    path('about', about, name='about'),
    path('profile/<username>', profile, name='profile'),
    path('profile/<username>/edit/', edit_profile, name='edit_profile'),

]
