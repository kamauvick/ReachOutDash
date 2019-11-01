from django.urls import path, include

from .views import landing, signup, index, create_chv, new_patient, new_emergency, access_status, edit_profile, profile

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('', landing, name='landing'),
    path('index', index, name='index'),
    path('new_chv', create_chv, name='new_chv'),
    path('new_patient', new_patient, name='new_patient'),
    path('new_emergency', new_emergency, name='new_emergency'),
    path('access_status', access_status, name='access_status'),
    path('profile/<username>', profile, name='profile'),
    path('profile/<username>/edit/', edit_profile, name='edit_profile'),
]
