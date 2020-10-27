from apps.shop.forms import CategoryForm, ListingForm, SubCategoryForm
from apps.shop.forms import ProductForm, UserReviewForm, TagForm
from apps.shop.models import Category, Payment, SubCategory, Tag, UserReview
from apps.shop.models import Product, Listing
from apps.service.models import DeliveryLocation
from apps.service.forms import DeliveryLocationForm
from django.shortcuts import render
from apps.accounts.models import User
from apps.seller.forms import VendorForm
from apps.accounts.forms import CreateVendorForm
from apps.seller.models import Vendor
from django.contrib.auth.models import Group
from django.contrib import messages
# Admin Home


def admin_home(request):
    user = request.user
    username = User.get_full_name(user)
    context = {'username': username}
    return render(request, 'home.html', context)


# Admin Vendor Management

def admin_create_vendor(request):
    form = CreateVendorForm()

    if request.method == 'POST':
        form = CreateVendorForm(request.POST)

        if form.is_valid():
            user = form.save()
            Group.objects.get_or_create(name="vendor")
            group = Group.objects.get(name="vendor")
            user.groups.add(group)
            gst = form.cleaned_data.get('gst_number')
            aadhar = form.cleaned_data.get('aadhar_number')
            name = form.cleaned_data.get('buisness_name')
            vendor = Vendor.objects.create(
                user=user, gst_number=gst,
                buisness_name=name, aadhar_number=aadhar)
            vendor.save()
            messages.success(request, f'{vendor} saved!')

    context = {'form': form}
    return render(request, 'create_vendor.html', context)


def admin_update_vendor(request, pk):
    form = VendorForm(instance=pk)

    if request.method == 'POST':
        form = VendorForm(request.POST, instance=pk)

        if form.is_valid():
            vendor = form.save()
            messages.success(request, f'{vendor} updated!')

    context = {'form': form}
    return render(request, 'update_vendor.html', context)


def admin_delete_vendor(request, pk):
    vendor = Vendor.objects.get(id=pk)
    if not vendor:
        messages.warning(request, "No Such Vendor")

    if request.method == 'POST':
        if vendor:
            name = vendor.buisness_name
            vendor.delete()
            messages.success(request, f'{name} Deleted!')
        else:
            messages.warning(request, "No Such Vendor")

    context = {'item': vendor}

    return render(request, 'delete_vendor.html', context)


def admin_list_vendor(request):
    vendors = Vendor.objects.all()
    context = {'vendors': vendors}
    return render(request, 'list_vendor.html', context)


def admin_detail_vendor(request, pk):
    vendor = Vendor.objects.get(id=pk)
    vd = User.objects.get(id=vendor)
    context = {'vendor': vendor, 'vd': vd}
    return render(request, 'detail_vendor.html', context)


# Category  Management

def admin_create_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save()
            messages.success(request, f'{category} created Successfully')

    context = {'form': form}
    return render(request, 'create_category.html', context)


def admin_update_category(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            category = form.save()
            messages.success(request, "Changes To Category Saved Successfully")

    context = {'form': form, 'category': category}
    return render(request, 'update_category.html', context)


def admin_delete_category(request, pk):
    category = Category.objects.get(id=pk)

    if not category:
        messages.warning(request, 'No Such Category')

    if request.method == 'POST':
        if category:
            category.delete()
            messages.success(request, "Category Deleted Successfully")
        else:
            messages.warning(request, 'No Such Category')

    context = {'item': category}
    return render(request, 'delete_category.html', context)


def admin_list_category(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'list_category.html', context)


def admin_detail_category(request, pk):
    categories = Category.objects.get(id=pk)
    tags = Tag.objects.filter(category=categories)
    subcat = SubCategory.objects.filter(parent=categories)
    context = {'categories': categories, 'tags': tags, 'subcat': subcat}
    return render(request, 'detail_category.html', context)

# Admin SubCategory Management


def admin_create_subcategory(request):
    form = SubCategoryForm()

    if request.method == 'POST':
        form = SubCategoryForm(request.POST)

        if form.is_valid():
            category = form.save()
            messages.success(request, f'{category} created Successfully')

    context = {'form': form}
    return render(request, 'create_subcategory.html', context)


def admin_update_subcategory(request, pk):
    category = SubCategory.objects.get(id=pk)
    form = SubCategoryForm(instance=category)

    if request.method == 'POST':
        form = SubCategoryForm(request.POST, instance=category)

        if form.is_valid():
            category = form.save()
            messages.success(request, "Changes To SubCategory Successful")

    context = {'form': form, 'category': category}
    return render(request, 'update_subcategory.html', context)


def admin_delete_subcategory(request, pk):
    category = SubCategory.objects.get(id=pk)

    if not category:
        messages.warning(request, 'No Such Subcategory')

    if request.method == 'POST':
        if category:
            category.delete()
            messages.success(request, "Sub Category Deleted Successfully")
        else:
            messages.warning(request, 'No Such Subcategory')

    context = {'item': category}
    return render(request, 'delete_subcategory.html', context)


def admin_list_subcategory(request):
    categories = SubCategory.objects.all()
    context = {'categories': categories}
    return render(request, 'list_subcategory.html', context)


def admin_detail_subcategory(request, pk):
    categories = SubCategory.objects.get(id=pk)
    tags = Tag.objects.filter(subcategory=categories)
    context = {'categories': categories, 'tags': tags}
    return render(request, 'detail_subcategory.html', context)


# Admin Tag Management

def admin_create_Tag(request):
    form = TagForm()

    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tag Created Successfully")

    context = {"form": form}
    return render(request, 'create_Tag.html', context)


def admin_update_Tag(request, pk):
    tag = Tag.objects.get(id=pk)
    form = TagForm(instance=tag)

    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes to Tag Saved Successfully")

    context = {"form": form, 'tag': tag}
    return render(request, 'update_Tag.html', context)


def admin_delete_Tag(request, pk):
    item = Tag.objects.get(id=pk)

    if not item:
        messages.warning(request, 'No Such Tag')
    if request.method == 'POST':
        if item:
            item = Tag.objects.get(id=pk)
            item.delete()
            messages.success(request, "Tag Deleted Successfully")
        else:
            messages.warning(request, 'No Such Tag')
    context = {"item": item}
    return render(request, 'delete_Tag.html', context)


def admin_list_Tag(request):
    tags = Tag.objects.all()
    context = {'tags': tags}
    return render(request, 'list_Tag.html', context)


# Admin Product Review Management

def admin_update_review(request, pk):
    form = UserReviewForm(instance=pk)

    if form.method == "POST":
        form = UserReviewForm(request.POST, instance=pk)

        if form.is_valid():
            form.save
            messages.success(request, 'Update Successful')
    context = {'form': form}
    return render(request, 'update_review.html', context)


def admin_delete_review(request, pk):
    item = UserReview.objects.get(id=pk)
    if not item:
        messages.warning(request, 'No Such Review')
    if request.method == 'POST':
        if item:
            item = UserReview.objects.get(id=pk)
            item.delete()
            messages.success(request, "Review Deleted Successfully")
        else:
            messages.warning(request, 'No Such Tag')
    context = {"item": item}
    return render(request, 'delete_review.html', context)


def admin_list_review(request):
    reviews = UserReview.objects.all()
    context = {'reviews': reviews}
    return render(request, 'list_review.html', context)


def admin_detail_review(request, pk):
    review = UserReview.objects.get(id=pk)
    context = {'review': review}
    return render(request, 'detail_review.html', context)


# Admin product Management

def admin_create_product(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Product Created Successfully")

    context = {"form": form}
    return render(request, 'create_product.html', context)


def admin_update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes Saved Successfully")

    context = {"form": form, "product": product}
    return render(request, 'update_product.html', context)


def admin_delete_product(request, pk):
    item = Product.objects.get(id=pk)
    if not item:
        messages.warning(request, 'No Such Product')
    if request.method == 'POST':
        if item:
            item = Product.objects.get(id=pk)
            item.delete()
            messages.success(request, "Product Deleted Successfully")
        else:
            messages.warning(request, 'No Such Product')
    context = {"item": item}
    return render(request, 'delete_product.html', context)


def admin_list_product(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'list_product.html', context)


def admin_detail_product(request, pk):
    product = Product.objects.get(id=pk)
    pre = UserReview.objects.filter(product=product).all
    ptag = Tag.objects.filter(product=product).all

    context = {
        "product": product,
        'ptag': ptag,
        'pre': pre
        }
    return render(request, 'detail_product.html', context)


# Admin listing Management

def admin_create_listing(request):
    form = ListingForm()

    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Listing Created Successfully")

    context = {"form": form}
    return render(request, 'create_listing.html', context)


def admin_update_listing(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes To Listing Saved Successfully")

    context = {"form": form}
    return render(request, 'update_listing.html', context)


def admin_delete_listing(request, pk):
    item = Listing.objects.get(id=pk)

    if not item:
        messages.warning(request, 'No Such Listing')
    if request.method == 'POST':
        if item:
            item = Listing.objects.get(id=pk)
            item.delete()
            messages.success(request, "Listing Deleted Successfully")
        else:
            messages.warning(request, 'No Such Listing')
    context = {"item": item}
    return render(request, 'delete_listing.html', context)


def admin_list_listing(request):
    listings = Listing.objects.all()
    products = Product.objects.filter(listing=listings)
    context = {'listings': listings, 'products': products}
    return render(request, 'list_listing.html', context)


def admin_detail_listing(request, pk):
    listing = Listing.objects.get(id=pk)
    vendor = Vendor.objects.get(id=listing.vendor)
    product = Product.objects.get(id=listing.product)

    context = {'listing': listing, 'vendor': vendor,
               'product': product}
    return render(request, 'detail_listing.html', context)
# Admin payment Management


def admin_list_payment(request):
    payments = Payment.objects.all()
    context = {'payments': payments}
    return render(request, 'list_payment.html', context)


def admin_detail_payment(request, pk):
    payment = Payment.objects.get(id=pk)
    context = {'payment': payment}
    return render(request, 'detail_payment.html', context)


# Admin location Management


def admin_create_location(request):
    form = DeliveryLocationForm()

    if request.method == 'POST':
        form = DeliveryLocationForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Service Location Added Successfully")

    context = {"form": form}
    return render(request, 'create_location.html', context)


def admin_update_location(request, pk):
    location = DeliveryLocation.objects.get(id=pk)
    form = DeliveryLocationForm(instance=location)

    if request.method == 'POST':
        form = DeliveryLocationForm(request.POST, instance=location)
        if form.is_valid:
            location = form.save()
            messages.success(request, "Changes To Service Location Successful")

    context = {"form": form, 'sl': location}
    return render(request, 'update_location.html', context)


def admin_delete_location(request, pk):
    item = DeliveryLocation.objects.get(id=pk)
    if not item:
        messages.warning(request, 'No Such Location')
    if request.method == 'POST':
        if item:
            item = DeliveryLocation.objects.get(id=pk)
            item.delete()
            messages.success(request, "Listing Deleted Successfully")
        else:
            messages.warning(request, 'No Such Location')
    context = {"item": item}
    return render(request, 'delete_location.html', context)


def admin_list_location(request):
    locations = DeliveryLocation.objects.all()
    context = {'locations': locations}
    return render(request, 'list_location.html', context)


def admin_detail_location(request, pk):
    location = DeliveryLocation.objects.get(pk)
    context = {'location': location}
    return render(request, 'detail_location.html', context)
