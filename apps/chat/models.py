from apps.seller.models import Vendor
from django.db import models


class AdminMessage(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    message = models.TextField()
    resolved = models.BooleanField(default=False)
    satisfied = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.vendor}'
