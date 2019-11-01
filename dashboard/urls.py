from django.urls import path, include

from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('signup/', signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
]
