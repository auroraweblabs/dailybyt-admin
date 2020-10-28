# from django.urls.conf import include
from base.views import home, registerCustomer, registerDelivery
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import user_login, logOut, registerAdmin, registerVendor


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', home, name="home"),
    path('',include('pwa.urls')),
    path('', user_login, name="login"),
    path('registerAdmin/', registerAdmin, name='register-admin'),
    path('registerVendor/', registerVendor, name='register-vendor'),
    path('registerCustomer/', registerCustomer, name='register-customer'),
    path('registerDelivery/', registerDelivery, name='register-delivery'),
    path('logout/', logOut, name="logout"),
    path('administration/', include('apps.admin.urls')),
    path('seller/', include('apps.seller.urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
