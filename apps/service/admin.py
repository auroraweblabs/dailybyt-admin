from django.contrib import admin
from .models import State, City, PinCode, Address, BankAccount
from .models import DeliveryLocation, PhoneOTP, EmailOTP

admin.site.register(State)
admin.site.register(City)
admin.site.register(PinCode)
admin.site.register(Address)
admin.site.register(BankAccount)
admin.site.register(DeliveryLocation)
admin.site.register(PhoneOTP)
admin.site.register(EmailOTP)
