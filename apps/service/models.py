from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class State(models.Model):
    name = models.CharField(verbose_name="State", max_length=50)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(verbose_name="City", max_length=50)

    def __str__(self):
        return self.name


class PinCode(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Pin Code", max_length=6)
    is_active = models.BooleanField(verbose_name="Service", default=True)

    def __str__(self):
        return self.title


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    line1 = models.CharField(verbose_name="Address Line 1",
                             max_length=50)
    line2 = models.CharField(verbose_name="Address Line 2",
                             max_length=50, blank=True)
    line3 = models.CharField(verbose_name="Address Line 3",
                             max_length=50, blank=True)
    landmark = models.CharField(verbose_name="Landmark",
                                max_length=30)
    pincode = models.ForeignKey(PinCode,
                                on_delete=models.CASCADE)
    city = models.ForeignKey(City,
                             on_delete=models.CASCADE)
    state = models.ForeignKey(State,
                              on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f' Line 1 : {self.line1}, User:{self.user}'


class DeliveryLocation(models.Model):
    pincode = models.ForeignKey(PinCode,
                                on_delete=models.CASCADE)

    city = models.ForeignKey(City,
                             on_delete=models.CASCADE)
    address = models.ForeignKey(Address,
                                on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Pin : {self.pincode}, Address: {self.address}'


class PhoneOTP(models.Model):
    phoneregex = RegexValidator(
        regex=r'^\+?1?\d{9,14}$',
        message="Phone Number Must be entered in Valid Format")

    phone = models.CharField(_('Phone Number'), validators=[phoneregex],
                             unique=True, max_length=15)

    otp = models.CharField(_('OTP'), max_length=9)

    count = models.IntegerField(_('Number of OTP Sent'),
                                default=0, help_text="Number of OTP Sent")

    logged = models.BooleanField(default=False,
                                 help_text=_("Was Verification Successful?"))

    forgot = models.BooleanField(default=False,
                                 help_text=_("Only True if Forgot Password"))

    forgot_logged = models.BooleanField(default=False,
                                        help_text=_("Master Reset Logged?"))

    def __str__(self):
        return str(self.phone) + ' is sent ' + str(self.otp)


class EmailOTP(models.Model):
    emailregex = RegexValidator(
        regex=r'\w[\w\.-]*@\w[\w\.-]+\.\w+',
        message="Phone Number Must be entered in Valid Format")
    email = models.CharField(_('E-mail'), max_length=24,
                             validators=[emailregex], unique=True)
    otp = models.CharField(_('OTP'), max_length=9)
    count = models.IntegerField(default=0)
    logged = models.BooleanField(default=False,
                                 help_text=_("Was Verification Successful?"))

    forgot = models.BooleanField(default=False,
                                 help_text=_("Only True if Forgot Password"))

    forgot_logged = models.BooleanField(default=False,
                                        help_text=_("Master Reset Logged?"))

    def __str__(self):
        return str(self.email) + ' is sent ' + str(self.otp)


class BankAccount(models.Model):
    acno = models.CharField(_('Account Number'), max_length=14)
    bname = models.CharField(_('Beneficiary Name'), max_length=50)
    ifsc = models.CharField(_('IFSC Code'), max_length=15)
    bank_name = models.CharField(_('Bank Name'), max_length=40)
    branch = models.CharField(_('Branch'), max_length=40)
    tnc = models.BooleanField(_('Terms of Use'), default=True)
    sub = models.BooleanField(_('Updates'), default=False)

    def __str__(self):
        return self.bname
