from django.db import models
from apps.service.models import Address, DeliveryLocation
from django.conf import settings


class Delivery(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name="Delivery",
                                on_delete=models.CASCADE, blank=True)
    aadhar_number = models.CharField(verbose_name="Aadhar Number",
                                     max_length=12, blank=True)
    service_areas = models.ManyToManyField(DeliveryLocation, blank=True)
    address = models.ForeignKey(Address, verbose_name='Address',
                                on_delete=models.CASCADE, blank=True,
                                null=True)

    @staticmethod
    def get_all_delivery_agents():
        return Delivery.objects.all()

    def __str__(self) -> str:
        return self.user.first_name
