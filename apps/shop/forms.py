from django import forms
from .models import Tag, Category, SubCategory, Product
from .models import Order, OrderItem, UserReview, Listing
from .models import Payment


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = (
            'name',
        )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'


class UserReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
