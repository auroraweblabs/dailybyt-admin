from django.contrib import admin
from .models import Tag, Category, SubCategory, Product
from .models import Order, OrderItem, UserReview, Listing
from .models import Payment


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(UserReview)
admin.site.register(Listing)
