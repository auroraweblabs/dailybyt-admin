from apps.admin.views import admin_create_Tag, admin_create_category
from apps.admin.views import admin_update_vendor, admin_home
from apps.admin.views import admin_delete_category, admin_delete_vendor
from apps.admin.views import admin_detail_category
from apps.admin.views import admin_detail_vendor, admin_list_category
from apps.admin.views import admin_list_vendor, admin_update_category
from apps.admin.views import admin_create_subcategory, admin_create_vendor
from apps.admin.views import admin_delete_subcategory, admin_detail_review
from apps.admin.views import admin_detail_subcategory, admin_list_Tag
from apps.admin.views import admin_list_review, admin_list_subcategory
from apps.admin.views import admin_update_Tag, admin_update_review
from apps.admin.views import admin_update_subcategory, admin_delete_Tag
from apps.admin.views import admin_delete_review, admin_create_listing
from apps.admin.views import admin_create_product, admin_delete_listing
from apps.admin.views import admin_delete_product, admin_detail_product
from apps.admin.views import admin_list_listing, admin_list_product
from apps.admin.views import admin_update_listing, admin_update_product
from apps.admin.views import admin_create_location, admin_delete_location
from apps.admin.views import admin_detail_location, admin_detail_payment
from apps.admin.views import admin_list_location, admin_list_payment
from apps.admin.views import admin_update_location, admin_detail_listing
from django.urls import path

urlpatterns = [
    # Home Path
    path('', admin_home, name='admin_home'),

    # Vendor Paths
    path('admin_create_vendor/',
         admin_create_vendor,
         name='admin_create_vendor'),

    path('admin_update_vendor/:<int:pk>',
         admin_update_vendor,
         name='admin_update_vendor'),

    path('admin_delete_vendor/:<int:pk>',
         admin_delete_vendor,
         name='admin_delete_vendor'),

    path('admin_list_vendor/',
         admin_list_vendor,
         name="admin_list_vendor"),

    path('admin_detail_vendor/<int:pk>',
         admin_detail_vendor,
         name="admin_detail_vendor"),

    # Category Paths
    path('admin_create_category/',
         admin_create_category,
         name='admin_create_category'),

    path('admin_update_category/<int:pk>',
         admin_update_category,
         name='admin_update_category'),

    path('admin_delete_category/:<int:pk>',
         admin_delete_category,
         name='admin_delete_category'),

    path('admin_list_category/',
         admin_list_category,
         name="admin_list_category"),

    path('admin_detail_category/<int:pk>',
         admin_detail_category,
         name="admin_detail_category"),

    # SubCategory Paths
    path('admin_create_subcategory/',
         admin_create_subcategory,
         name='admin_create_subcategory'),

    path('admin_update_subcategory/<int:pk>',
         admin_update_subcategory,
         name='admin_update_subcategory'),

    path('admin_delete_subcategory/:<int:pk>',
         admin_delete_subcategory,
         name='admin_delete_subcategory'),

    path('admin_list_subcategory/',
         admin_list_subcategory,
         name="admin_list_subcategory"),

    path('admin_detail_subcategory/<int:pk>',
         admin_detail_subcategory,
         name="admin_detail_subcategory"),

    # Tag Paths
    path('admin_create_tag/',
         admin_create_Tag,
         name='admin_create_tag'),

    path('admin_update_tag/<int:pk>',
         admin_update_Tag,
         name='admin_update_tag'),

    path('admin_delete_tag/:<int:pk>',
         admin_delete_Tag,
         name='admin_delete_tag'),

    path('admin_list_tag/',
         admin_list_Tag,
         name="admin_list_tag"),

    # Review Paths

    path('admin_update_review/<int:pk>',
         admin_update_review,
         name='admin_update_review'),

    path('admin_delete_review/:<int:pk>',
         admin_delete_review,
         name='admin_delete_review'),

    path('admin_list_review/',
         admin_list_review,
         name="admin_list_review"),

    path('admin_detail_review/<int:pk>',
         admin_detail_review,
         name="admin_detail_review"),

    # Product Paths

    path('admin_create_product/',
         admin_create_product,
         name='admin_create_product'),

    path('admin_update_product/<int:pk>',
         admin_update_product,
         name='admin_update_product'),

    path('admin_delete_product/:<int:pk>',
         admin_delete_product,
         name='admin_delete_product'),

    path('admin_list_product/',
         admin_list_product,
         name="admin_list_product"),

    path('admin_detail_product/<int:pk>',
         admin_detail_product,
         name="admin_detail_product"),

    # Listing Paths

    path('admin_create_listing/',
         admin_create_listing,
         name='admin_create_listing'),

    path('admin_update_listing/<int:pk>',
         admin_update_listing,
         name='admin_update_listing'),

    path('admin_delete_listing/:<int:pk>',
         admin_delete_listing,
         name='admin_delete_listing'),

    path('admin_list_listing/',
         admin_list_listing,
         name="admin_list_listing"),

    path('admin_detail_listing/',
         admin_detail_listing,
         name="admin_detail_listing"),

    # Payment Paths
    path('admin_list_payment/',
         admin_list_payment,
         name="admin_list_payment"),

    path('admin_detail_payment/<int:pk>',
         admin_detail_payment,
         name="admin_detail_payment"),

    # Product Paths

    path('admin_create_location/',
         admin_create_location,
         name='admin_create_location'),

    path('admin_update_location/<int:pk>',
         admin_update_location,
         name='admin_update_location'),

    path('admin_delete_location/:<int:pk>',
         admin_delete_location,
         name='admin_delete_location'),

    path('admin_list_location/',
         admin_list_location,
         name="admin_list_location"),

    path('admin_detail_location/<int:pk>',
         admin_detail_location,
         name="admin_detail_location"),

]
