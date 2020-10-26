from django.db import models
from apps.service.models import Address
from django.conf import settings


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
    address = models.ManyToManyField(Address, verbose_name='Address',
                                     blank=True)

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
