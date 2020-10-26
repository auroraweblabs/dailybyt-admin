from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.accounts.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['phone', 'email', 'password1', 'password2',
                  'first_name', 'last_name', 'avatar']


class CreateVendorForm(CreateUserForm):
    buisness_name = forms.CharField(label="Buisness Name")
    aadhar_number = forms.CharField(label="Aadhar Number")
    gst_number = forms.CharField(label="GST Number")


class CreateCustomerForm(CreateUserForm):
    aadhar_number = forms.CharField(label="Aadhar Number")


class CreateDeliveryForm(CreateUserForm):
    aadhar_number = forms.CharField(label="Aadhar Number")
