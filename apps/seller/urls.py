from apps.seller.views import vendor_home
from django.urls import path


urlpatterns = [
    path('', vendor_home, name="vendor_home")
]
