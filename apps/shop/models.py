from django.db import models


class UserReview(models.Model):
    choices = (
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'decent'),
        ('4', 'good'),
        ('5', 'amazing')
    )
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    rating = models.CharField(max_length=10, choices=choices)

    @staticmethod
    def get_all_reviews():
        return UserReview.objects.all()

    @staticmethod
    def get_review_from_rating(rating):
        return UserReview.objects.filter(rating=rating)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def get_all_tags():
        return Tag.objects.all()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    commission = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    is_digital = models.BooleanField(default=False)
    tags = models.ManyToManyField("shop.Tag")

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    @staticmethod
    def get_commission_on_category(category_id):
        if category_id:
            return float(Category.objects.filter(category_id).commission)

    @staticmethod
    def get_all_tags(self):
        return self.tags.all()

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100, null=True)
    parent = models.ForeignKey("shop.Category", on_delete=models.SET_NULL,
                               null=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    @staticmethod
    def get_all_subcategories():
        return SubCategory.objects.all()

    @staticmethod
    def get_all_tags(self):
        return self.tags.all()

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_on = models.DateField(auto_now=True, auto_now_add=False)
    image1 = models.ImageField(
        upload_to='productImages/', null=True, blank=True)
    image2 = models.ImageField(
        upload_to='productImages/', null=True, blank=True)
    image3 = models.ImageField(
        upload_to='productImages/', null=True, blank=True)
    image4 = models.ImageField(
        upload_to='productImages/', null=True, blank=True)
    category = models.ForeignKey(
        "shop.Category", on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(
        "shop.SubCategory", on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField("shop.Tag")
    reviews = models.ManyToManyField("shop.UserReview", blank=True)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_all_products_by_subcategoryid(category_id):
        if category_id:
            return Product.objects.filter(subcategory=category_id)
        else:
            return Product.get_all_products()

    def __str__(self):
        return self.title


class Listing(models.Model):

    vendor = models.ForeignKey("seller.Vendor", on_delete=models.DO_NOTHING)
    product = models.ForeignKey("shop.Product", on_delete=models.DO_NOTHING)
    quantity = models.DecimalField(verbose_name="Quantity",
                                   decimal_places=0, max_digits=10)
    price = models.FloatField(verbose_name="Listing Price")

    @staticmethod
    def get_all_listings():

        return Listing.objects.all()

    @staticmethod
    def get_all_listing_by_vendor(vendor):
        return Listing.objects.filter(vendor=vendor)

    @staticmethod
    def get_all_listing_by_product(product):
        return Listing.objects.filter(product=product)

    @staticmethod
    def get_all_listing_by_price(price):
        return Listing.objects.filter(price < price)

    def __str__(self):
        return self.vendor


class Order(models.Model):

    customer = models.ForeignKey("customer.Customer",
                                 on_delete=models.DO_NOTHING)
    products = models.ManyToManyField("shop.Listing")
    delivery = models.ForeignKey("delivery.Delivery",
                                 on_delete=models.DO_NOTHING)
    value = models.FloatField()
    payment_status = models.BooleanField(
        default=False, verbose_name="Paid/Unpaid ?")
    delivery_status = models.BooleanField(
        default=False, verbose_name="Delivered/Not ?")

    @staticmethod
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum[(item.quantity for item in orderitems)]
        return total

    @staticmethod
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum[(item.get_total for item in orderitems)]
        return total

    @staticmethod
    def get_total_commission(self):
        orderitems = self.orderitems_set.all()
        com = 0
        for item in orderitems:
            com += item.product.price * \
                ((item.product.category.commission) / 100)
        return com

    @staticmethod
    def get_gst(self):
        gst = self.get_total_commission() * (0.18)
        return gst

    @staticmethod
    def vendor_amount(self):
        total = self.get_cart_total - self.get_total_commission - self.get_gst
        return total

    @staticmethod
    def get_ready_orders(self):
        orderitems = self.orderitem.set.all()
        orderitems.filter(payment_status=True, delivery_status=False)

    def __str__(self):
        return str(self.customer)


class OrderItem(models.Model):

    product = models.ForeignKey("shop.Product", on_delete=models.SET_NULL,
                                null=True)
    order = models.ForeignKey("shop.Order", on_delete=models.SET_NULL,
                              null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)

    @staticmethod
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class SaleReport(models.Model):
    vendor = models.ForeignKey("seller.Vendor", on_delete=models.DO_NOTHING)
    order = models.ForeignKey("shop.Order", on_delete=models.DO_NOTHING)
    products = models.ManyToManyField("shop.Product")
    value = models.DecimalField(max_digits=10, default=0, decimal_places=2)
    commission = models.DecimalField(max_digits=10, default=0, decimal_places=2)


class Payment(models.Model):

    choices = (
        ('paid', 'Paid'),
        ('unpaid', 'Unpaid'),
        ('cod', 'cod'),
    )
    order = models.ForeignKey("shop.Order", on_delete=models.SET_NULL,
                              null=True)
    status = models.CharField(max_length=40, choices=choices)
    delivered = models.BooleanField(default=False)
