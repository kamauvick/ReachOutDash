from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Chv, Patient, Emergencies, Location


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ChvForm(forms.ModelForm):
    class Meta:
        model = Chv
        fields = ['name', 'age', 'phonenumber', 'location']


class UpdateChvForm(forms.ModelForm):
    class Meta:
        model = Chv
        exclude = ()


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'examiner', 'age', 'gender', 'location', 'time', 'symptoms', 'urgency', 'action_taken']


class EmergencyForm(forms.ModelForm):
    class Meta:
        model = Emergencies
        fields = ['type', 'location', 'reported_by']


class RoadStatusForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'county', 'accessibility']
