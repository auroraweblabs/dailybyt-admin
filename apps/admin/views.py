from apps.customer.models import Customer
from apps.shop.forms import CategoryForm, ListingForm, SubCategoryForm
from apps.shop.forms import ProductForm, UserReviewForm, TagForm
from apps.shop.models import Category, Order, Payment, SaleReport, SaleReportToday, SaleReportYesterday, SubCategory, Tag, UserReview
from apps.shop.models import Product, Listing
from apps.service.models import DeliveryLocation, SupportMessage
from apps.service.forms import DeliveryLocationForm
from django.shortcuts import redirect, render
from apps.accounts.models import User
from apps.seller.forms import VendorForm
from apps.accounts.forms import CreateVendorForm
from apps.seller.models import Vendor, VendorToday
from django.contrib.auth.models import Group
from django.contrib import messages
# Admin Home


def admin_home(request):
    user = request.user
    category = Category.objects.all().count()
    subcategory = SubCategory.objects.all().count()
    vendor = Vendor.objects.all().count()
    products = Product.objects.all().count()
    servicelocation = DeliveryLocation.objects.all().count()
    listing = Listing.objects.all().count()
    order = Order.objects.all().count()
    username = User.get_full_name(user)
    customer = Customer.objects.all().count()
    vendor_today = Vendor.today.all().count()
    vendor_yesterday = Vendor.yesterday.all().count()
    vendor_week = Vendor.week.all().count()
    customer_today = Customer.today.all().count()
    customer_yesterday = Customer.yesterday.all().count()
    customer_week = Customer.week.all().count()
    order_today = Order.today.all().count()
    order_yesterday = Order.yesterday.all().count()
    order_week = Order.week.all().count()
    sale_today = SaleReport.today.all().count()
    sale_yesterday = SaleReport.yesterday.all().count()
    sale_week = SaleReport.week.all().count()

    context = {
        'username': username,
        'category':category,
        'subcategory':subcategory,
        'products':products,
        'vendor':vendor,
        'listing':listing,
        'servicelocation':servicelocation,
        'order':order,
        'customer':customer,
        'vendor_today':vendor_today,
        'vendor_yesterday':vendor_yesterday,
        'vendor_week':vendor_week,
        'customer_today':customer_today,
        'customer_yesterday':customer_yesterday,
        'customer_week':customer_week,
        'order_today':order_today,
        'order_yesterday':order_yesterday,
        'order_week':order_week,
        'sale_today':sale_today,
        'sale_yesterday':sale_yesterday,
        'sale_week':sale_week,
        }
    return render(request, 'administrator/home.html', context)


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
            return redirect('admin_list_vendor')

    context = {'form': form}
    return render(request, 'administrator/create_vendor.html', context)


def admin_update_vendor(request, pk):
    vendor = Vendor.objects.get(id=pk)
    form = VendorForm(instance=vendor)

    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)

        if form.is_valid():
            vendor = form.save()
            messages.success(request, f'{vendor} updated!')
            return redirect('admin_list_vendor')

    context = {'form': form}
    return render(request, 'administrator/edit_vendor.html', context)


def admin_delete_vendor(request, pk):
    vendor = Vendor.objects.get_or_404(id=pk)
    if not vendor:
        messages.warning(request, "No Such Vendor")
        return redirect('admin_list_vendor')

    if request.method == 'POST':
        if vendor:
            name = vendor.buisness_name
            vendor.delete()
            messages.success(request, f'{name} Deleted!')
            return redirect('admin_list_vendor')
        else:
            messages.warning(request, "No Such Vendor")
            return redirect('admin_list_vendor')

    context = {'item': vendor}

    return render(request, 'administrator/delete_vendor.html', context)


def admin_list_vendor(request):
    vendors = Vendor.objects.all()
    context = {'vendors': vendors}
    return render(request, 'administrator/list_vendor.html', context)


def admin_detail_vendor(request, pk):
    vendor = Vendor.objects.get(id=pk)
    vd = User.objects.get(id=vendor)
    context = {'vendor': vendor, 'vd': vd}
    return render(request, 'administrator/detail_vendor.html', context)


# Category  Management

def admin_create_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save()
            messages.success(request, f'{category} created Successfully')
            return redirect('admin_list_category')

    context = {'form': form}
    return render(request, 'administrator/create_category.html', context)


def admin_update_category(request, pk):
    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            category = form.save()
            messages.success(request, "Changes To Category Saved Successfully")
            return redirect('admin_list_category')

    context = {'form': form, 'category': category}
    return render(request, 'administrator/update_category.html', context)


def admin_delete_category(request, pk):
    category = Category.objects.get(id=pk)

    if not category:
        messages.warning(request, 'No Such Category')
        return redirect('admin_list_category')

    if request.method == 'POST':
        if category:
            category.delete()
            messages.success(request, "Category Deleted Successfully")
            return redirect('admin_list_category')
        else:
            messages.warning(request, 'No Such Category')
            return redirect('admin_list_category')

    context = {'item': category}
    return render(request, 'administrator/delete_category.html', context)



def admin_list_category(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'administrator/list_category.html', context)


def admin_detail_category(request, pk):
    categories = Category.objects.get(id=pk)
    tags = Tag.objects.filter(category=categories)
    subcat = SubCategory.objects.filter(parent=categories)
    context = {'categories': categories, 'tags': tags, 'subcat': subcat}
    return render(request, 'administrator/detail_category.html', context)

# Admin SubCategory Management


def admin_create_subcategory(request):
    form = SubCategoryForm()

    if request.method == 'POST':
        form = SubCategoryForm(request.POST)

        if form.is_valid():
            category = form.save()
            messages.success(request, f'{category} created Successfully')
            return redirect('admin_list_subcategory')

    context = {'form': form}
    return render(request, 'administrator/create_subcategory.html', context)


def admin_update_subcategory(request, pk):
    category = SubCategory.objects.get(id=pk)
    form = SubCategoryForm(instance=category)

    if request.method == 'POST':
        form = SubCategoryForm(request.POST, instance=category)

        if form.is_valid():
            category = form.save()
            messages.success(request, "Changes To SubCategory Successful")
            return redirect('admin_list_subcategory')

    context = {'form': form, 'category': category}
    return render(request, 'administrator/update_subcategory.html', context)


def admin_delete_subcategory(request, pk):
    category = SubCategory.objects.get_or_404(id=pk)

    if not category:
        messages.warning(request, 'No Such Subcategory')
        return redirect('admin_list_subcategory')

    if request.method == 'POST':
        if category:
            category.delete()
            messages.success(request, "Sub Category Deleted Successfully")
            return redirect('admin_list_subcategory')
        else:
            messages.warning(request, 'No Such Subcategory')
            return redirect('admin_list_subcategory')

    context = {'item': category}
    return render(request, 'administrator/delete_subcategory.html', context)


def admin_list_subcategory(request):
    categories = SubCategory.objects.all()
    context = {'categories': categories}
    return render(request, 'administrator/list_subcategory.html', context)


def admin_detail_subcategory(request, pk):
    categories = SubCategory.objects.get(id=pk)
    tags = Tag.objects.filter(subcategory=categories)
    context = {'categories': categories, 'tags': tags}
    return render(request, 'administrator/detail_subcategory.html', context)


# Admin Tag Management

def admin_create_Tag(request):
    form = TagForm()

    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tag Created Successfully")
            return redirect('admin_list_tag')

    context = {"form": form}
    return render(request, 'administrator/create_tag.html', context)


def admin_update_Tag(request, pk):
    tag = Tag.objects.get(id=pk)
    form = TagForm(instance=tag)

    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes to Tag Saved Successfully")
            return redirect('admin_list_tag')

    context = {"form": form, 'tag': tag}
    return render(request, 'administrator/update_tag.html', context)


def admin_delete_Tag(request, pk):
    item = Tag.objects.get_or_404(id=pk)

    if not item:
        messages.warning(request, 'No Such Tag')
        return redirect('admin_list_tag')
    if request.method == 'POST':
        if item:
            item = Tag.objects.get(id=pk)
            item.delete()
            messages.success(request, "Tag Deleted Successfully")
            return redirect('admin_list_tag')
        else:
            messages.warning(request, 'No Such Tag')
            return redirect('admin_list_tag')
    context = {"item": item}
    return render(request, 'administrator/delete_tag.html', context)


def admin_list_Tag(request):
    tags = Tag.objects.all()
    context = {'tags': tags}
    return render(request, 'administrator/list_tag.html', context)


# Admin Product Review Management

def admin_update_review(request, pk):
    form = UserReviewForm(instance=pk)

    if form.method == "POST":
        form = UserReviewForm(request.POST, instance=pk)

        if form.is_valid():
            form.save
            messages.success(request, 'Update Successful')
            return redirect('admin_list_review')
    context = {'form': form}
    return render(request, 'administrator/update_review.html', context)


def admin_delete_review(request, pk):
    item = UserReview.objects.get(id=pk)
    if not item:
        messages.warning(request, 'No Such Review')
        return redirect('admin_list_userreview')
    if request.method == 'POST':
        if item:
            item = UserReview.objects.get(id=pk)
            item.delete()
            messages.success(request, "Review Deleted Successfully")
            return redirect('admin_list_userreview')
        else:
            messages.warning(request, 'No Such Tag')
            return redirect('admin_list_userreview')
    context = {"item": item}
    return render(request, 'administrator/delete_review.html', context)


def admin_list_review(request):
    reviews = UserReview.objects.all()
    context = {'reviews': reviews}
    return render(request, 'administrator/list_review.html', context)


def admin_detail_review(request, pk):
    review = UserReview.objects.get(id=pk)
    context = {'review': review}
    return render(request, 'administrator/detail_review.html', context)


# Admin product Management

def admin_create_product(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Product Created Successfully")
            return redirect('admin_list_product')

    context = {"form": form}
    return render(request, 'administrator/create_product.html', context)


def admin_update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes Saved Successfully")
            return redirect('admin_list_product')

    context = {"form": form, "product": product}
    return render(request, 'administrator/update_product.html', context)


def admin_delete_product(request, pk):
    item = Product.objects.get(id=pk)
    if not item:
        messages.warning(request, 'No Such Product')
    if request.method == 'POST':
        if item:
            item = Product.objects.get(id=pk)
            item.delete()
            messages.success(request, "Product Deleted Successfully")
            return redirect('admin_list_product')
        else:
            messages.warning(request, 'No Such Product')
            return redirect('admin_list_product')
    context = {"item": item}
    return render(request, 'administrator/delete_product.html', context)


def admin_list_product(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'administrator/list_product.html', context)


def admin_detail_product(request, pk):
    product = Product.objects.get(id=pk)
    pre = UserReview.objects.filter(product=product).all
    ptag = Tag.objects.filter(product=product).all

    context = {
        "product": product,
        'ptag': ptag,
        'pre': pre
        }
    return render(request, 'administrator/detail_product.html', context)


# Admin listing Management

def admin_create_listing(request):
    form = ListingForm()

    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Listing Created Successfully")
            return redirect('admin_list_listing')

    context = {"form": form}
    return render(request, 'administrator/create_listing.html', context)


def admin_update_listing(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes To Listing Saved Successfully")
            return redirect('admin_list_listing')

    context = {"form": form}
    return render(request, 'administrator/update_listing.html', context)


def admin_delete_listing(request, pk):
    item = Listing.objects.get_or_404(id=pk)

    if not item:
        messages.warning(request, 'No Such Listing')
    if request.method == 'POST':
        if item:
            item = Listing.objects.get(id=pk)
            item.delete()
            messages.success(request, "Listing Deleted Successfully")
            return redirect('admin_list_listing')
        else:
            messages.warning(request, 'No Such Listing')
            return redirect('admin_list_listing')
    context = {"item": item}
    return render(request, 'administrator/delete_listing.html', context)


def admin_list_listing(request):
    listings = Listing.objects.all()
    products = Product.objects.filter(listing=listings)
    context = {'listings': listings, 'products': products}
    return render(request, 'administrator/list_listing.html', context)


def admin_detail_listing(request, pk):
    listing = Listing.objects.get(id=pk)
    vendor = Vendor.objects.get(id=listing.vendor)
    product = Product.objects.get(id=listing.product)

    context = {
        'listing': listing,
        'vendor': vendor,
        'product': product
        }
    return render(request, 'administrator/detail_listing.html', context)
# Admin payment Management


def admin_list_payment(request):
    payments = Payment.objects.all()
    context = {'payments': payments}
    return render(request, 'administrator/list_payments.html', context)


def admin_detail_payment(request, pk):
    payment = Payment.objects.get(id=pk)
    context = {'payment': payment}
    return render(request, 'administrator/detail_payments.html', context)


# ADmin Order 
def admin_list_order(request):
    order = Order.objects.all()
    context = {'order': order}
    return render(request, 'administrator/list_order.html', context)


def admin_detail_order(request, pk):
    order = Order.objects.get(id=pk)
    context = {'order': order}
    return render(request, 'administrator/detail_order.html', context)

# ADmin support
def admin_list_support(request):
    support = SupportMessage.objects.all()
    context = {'support': support}
    return render(request, 'administrator/list_support.html', context)


def admin_detail_support(request, pk):
    support = SupportMessage.objects.get(id=pk)
    context = {'support': support}
    return render(request, 'administrator/detail_support.html', context)


# Admin location Management


def admin_create_location(request):
    form = DeliveryLocationForm()

    if request.method == 'POST':
        form = DeliveryLocationForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Service Location Added Successfully")
            return redirect('admin_list_location')

    context = {"form": form}
    return render(request, 'administrator/create_servicelocation.html', context)


def admin_update_location(request, pk):
    location = DeliveryLocation.objects.get(id=pk)
    form = DeliveryLocationForm(instance=location)

    if request.method == 'POST':
        form = DeliveryLocationForm(request.POST, instance=location)
        if form.is_valid:
            location = form.save()
            messages.success(request, "Changes To Service Location Successful")
            return redirect('admin_list_location')

    context = {"form": form, 'sl': location}
    return render(request, 'administrator/edit_servicelocation.html', context)


def admin_delete_location(request, pk):
    item = DeliveryLocation.objects.get_or_404(id=pk)
    if not item:
        messages.warning(request, 'No Such Location')
        return redirect('admin_list_location')
    if request.method == 'POST':
        if item:
            item = DeliveryLocation.objects.get(id=pk)
            item.delete()
            messages.success(request, "Listing Deleted Successfully")
            return redirect('admin_list_location')
        else:
            messages.warning(request, 'No Such Location')
            return redirect('admin_list_location')
    context = {"item": item}
    return render(request, 'administrator/delete_servicelocation.html', context)


def admin_list_location(request):
    locations = DeliveryLocation.objects.all()
    context = {'locations': locations}
    return render(request, 'administrator/list_servicelocation.html', context)


def admin_detail_location(request, pk):
    location = DeliveryLocation.objects.get(pk)
    context = {'location': location}
    return render(request, 'administrator/detail_servicelocation.html', context)
