from django.db import models
from datetime import date,timedelta
from django.utils import timezone
from django.conf import settings

class CustomerToday(models.Manager):
    def get_queryset(self):
        today = date.today()
        return super(CustomerToday, self).get_queryset().filter(added_on__gte=today)
    
class CustomerYesterday(models.Manager):
    def get_queryset(self):
        today = date.today()
        yesterday = (today - timedelta(1))
        return super(CustomerYesterday, self).get_queryset().filter(added_on__range=(yesterday,today))


class CustomerThisWeek(models.Manager):
    def get_queryset(self):
        added_on = models.DateTimeField(default=timezone.now)
        today = date.today()
        week = (today - timedelta(7))
        return super(CustomerThisWeek, self).get_queryset().filter(added_on__gt=week)


class Customer(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name="Customer",
                                on_delete=models.CASCADE)
    aadhar_number = models.CharField(verbose_name="Aadhar Number",
                                     max_length=12, blank=True)
    balance = models.DecimalField(verbose_name="Wallet Balance",
                                  max_digits=10,
                                  decimal_places=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    last_accessed_at = models.DateTimeField(auto_now=True, blank=True)
    address = models.ManyToManyField("service.Address", verbose_name='Address',
                                     blank=True)
    added_on = models.DateTimeField(default=timezone.now)
    
    objects= models.Manager()
    today = CustomerToday()
    yesterday = CustomerYesterday()
    week = CustomerThisWeek()                                 

    @staticmethod
    def get_balance(self):
        return self.balance

    @staticmethod
    def add_money(self, amount):
        if amount:
            self.balance += amount

    @staticmethod
    def make_payment(self, amount):
        if amount and self.balance:
            self.balance -= amount

    def __str__(self) -> str:
        return self.user.first_name
