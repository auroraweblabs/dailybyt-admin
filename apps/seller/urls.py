from apps.seller.views import vendor_add_bank_account, vendor_add_gst
from apps.seller.views import vendor_home, vendor_register_nogst
from apps.seller.views import vendor_send_otp, vendor_verify_gst
from apps.seller.views import vendor_verify_otp, vendor_add_service_location
from apps.seller.views import vendor_verify_location, vendor_register_withgst
from apps.seller.views import vendor_create_listing, vendor_create_location
from apps.seller.views import vendor_create_product, vendor_update_product
from apps.seller.views import vendor_delete_listing, vendor_list_listings
from apps.seller.views import vendor_detail_listing, vendor_detail_location
from apps.seller.views import vendor_detail_order, vendor_detail_payment
from apps.seller.views import vendor_detail_product, vendor_detail_report
from apps.seller.views import vendor_create_support_message, vendor_list_orders
from apps.seller.views import vendor_delete_support_message
from apps.seller.views import vendor_detail_support_message
from apps.seller.views import vendor_list_payments, vendor_list_products
from apps.seller.views import vendor_list_locations, vendor_update_listing
from apps.seller.views import vendor_update_support_message
from apps.seller.views import vendor_list_support_messages
from apps.seller.views import vendor_update_location
from apps.seller.views import vendor_list_reports

from django.urls import path


urlpatterns = [
    path('', vendor_home, name="vendor_home"),
    path('register_with_gst/',
         vendor_register_withgst,
         name="vendor_register_with_gst"),
    path('register_nogst/',
         vendor_register_nogst,
         name="vendor_register_nogst"),
    path('add_gst/<int:pk>',
         vendor_add_gst,
         name='vendor_add_gst'),
    path('verify_gst/<int:pk>',
         vendor_verify_gst,
         name='vendor_verify_gst'),
    path('verify_location/<int:pk>',
         vendor_verify_location,
         name='vendor_verify_location'),
    path('add_location/',
         vendor_add_service_location,
         name='vendor_add_location/'),
    path('send_otp/<int:pk>',
         vendor_send_otp,
         name='vendor_send_otp'),
    path('verify_otp/<int:pk>',
         vendor_verify_otp,
         name='vendor_verify_otp'),
    path('add_bank_account/<int:pk>',
         vendor_add_bank_account,
         name="vendor_add_bank_account"),
    path('create_product/',
         vendor_create_product,
         name="vendor_create_product"),
    path('create_listing/',
         vendor_create_listing,
         name="vendor_create_product"),
    path('create_location/',
         vendor_create_location,
         name="vendor_create_location"),
    path('create_support_message/',
         vendor_create_support_message,
         name="vendor_create_support_message"),
    path('update_product/<int:pk>',
         vendor_update_product,
         name="vendor_update_product"),
    path('update_listing/<int:pk>',
         vendor_update_listing,
         name="vendor_update_listing"),
    path('update_locatopm/<int:pk>',
         vendor_update_location,
         name="vendor_update_location"),
    path('update_support_message/<int:pk>',
         vendor_update_support_message,
         name="vendor_update_support_message"),
    path('delete_listing/<int:pk>',
         vendor_delete_listing,
         name="vendor_delete_listing"),
    path('delete_support_message/<int:pk>',
         vendor_delete_support_message,
         name="vendor_delete_support_message"),
    path('list_listings/',
         vendor_list_listings,
         name="vendor_list_listings"),
    path('list_locations/',
         vendor_list_locations,
         name="vendor_list_locations"),
    path('list_orders/',
         vendor_list_orders,
         name="vendor_list_orders"),
    path('list_payments/',
         vendor_list_payments,
         name="vendor_list_payments"),
    path('list_reports/',
         vendor_list_reports,
         name="vendor_list_reports"),
    path('list_support_messages/',
         vendor_list_support_messages,
         name="vendor_list_support_messages"),
    path('list_products/',
         vendor_list_products,
         name="vendor_list_products"),
    path('detail_listing/<int:pk>',
         vendor_detail_listing,
         name="vendor_detail_listing"),
    path('detail_location/<int:pk>',
         vendor_detail_location,
         name="vendor_detail_location"),
    path('detail_order/<int:pk>',
         vendor_detail_order,
         name="vendor_detail_order"),
    path('detail_product/<int:pk>',
         vendor_detail_product,
         name="vendor_detail_product"),
    path('detail_report/<int:pk>',
         vendor_detail_report,
         name="vendor_detail_report"),
    path('detail_support_message/<int:pk>',
         vendor_detail_support_message,
         name="vendor_detail_support_message"),
    path('detail_payment/<int:pk>',
         vendor_detail_payment,
         name="vendor_detail_payment"),

]
