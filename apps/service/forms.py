from django import forms
from .models import State, City, PinCode, Address, BankAccount
from .models import DeliveryLocation, PhoneOTP, EmailOTP


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ('name')


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('name')


class PinCodeForm(forms.ModelForm):
    class Meta:
        model = PinCode
        fields = ('city', 'title')


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            'user',
            'line1',
            'line2',
            'line3',
            'landmark',
            'pincode',
            'city',
            'state')


class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = (
            'acno',
            'ifsc',
            'bname',
            'bank_name',
            'branch',
            'tnc',
            'sub')


class DeliveryLocationForm(forms.ModelForm):
    class Meta:
        model = DeliveryLocation
        fields = (
            'pincode',
            'city',
            'address',
            'is_active')


class PhoneOTPForm(forms.ModelForm):
    class Meta:
        model = PhoneOTP
        fields = (
            'phone',
            'otp')


class EmailOTPForm(forms.ModelForm):
    class Meta:
        model = EmailOTP
        fields = (
            'email',
            'otp')
