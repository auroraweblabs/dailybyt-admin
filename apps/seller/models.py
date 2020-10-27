from django.db import models
from apps.service.models import Address, BankAccount, DeliveryLocation
from django.conf import settings


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

    @staticmethod
    def get_all_vendors():
        return Vendor.objects.all()

    def __str__(self) -> str:
        return self.buisness_name
