from django.db import models
from apps.service.models import Address, BankAccount, DeliveryLocation
from django.utils import timezone
from datetime import datetime, timedelta,date
from django.conf import settings

class VendorToday(models.Manager):
    def get_queryset(self):
        today = date.today()
        return super(VendorToday, self).get_queryset().filter(added_on__gte=today)
    
class VendorYesterday(models.Manager):
    def get_queryset(self):
        today = date.today()
        yesterday = (today - timedelta(1))
        return super(VendorYesterday, self).get_queryset().filter(added_on__range=(yesterday,today))


class VendorThisWeek(models.Manager):
    def get_queryset(self):
        added_on = models.DateTimeField(default=timezone.now)
        today = date.today()
        week = (today - timedelta(7))
        return super(VendorThisWeek, self).get_queryset().filter(added_on__gt=week)


class Vendor(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name="Vendor",
                                on_delete=models.CASCADE)
    buisness_name = models.CharField(verbose_name="Buisness Name",
                                     max_length=255, blank=True)
    aadhar_number = models.CharField(verbose_name="Aadhar Number",
                                     max_length=12, blank=True)
    gst_number = models.CharField(verbose_name="GST Number",
                                  max_length=15, blank=True)
    bank_account = models.ForeignKey(BankAccount,
                                     on_delete=models.CASCADE,
                                     blank=True,
                                     null=True)
    service_areas = models.ManyToManyField(DeliveryLocation, blank=True)
    address = models.ForeignKey(Address, verbose_name='Address',
                                on_delete=models.CASCADE,
                                null=True, blank=True)
    added_on = models.DateTimeField(default=timezone.now)
    
    objects= models.Manager()
    today = VendorToday()
    yesterday = VendorYesterday()
    week = VendorThisWeek()

    @staticmethod
    def get_all_vendors():
        return Vendor.objects.all()

    def __str__(self) -> str:
        return self.buisness_name



    
