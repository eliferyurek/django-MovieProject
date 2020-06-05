from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'username', 'email']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class AddressForm(ModelForm):
    class Meta:
        model = AddressCustomer
        fields = ['addres', 'city']


class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ['address', 'city']


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'


class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'
