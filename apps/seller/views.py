from django.http import request
from django.shortcuts import render
from apps.seller.models import Vendor
from apps.shop.models import Listing, Order, Product, SaleReport, Tag
from apps.shop.models import UserReview, Payment
from apps.shop.forms import ListingForm, ProductForm
from apps.service.models import DeliveryLocation, SupportMessage
from apps.service.forms import DeliveryLocationForm, SupportMessageForm
from django.contrib import messages


# Exclusive Views for Vendors
def vendor_home(request):
    vendor = Vendor.objects.all()
    context = {'vendor': vendor}
    print(vendor)
    return render(request, 'vendor/home.html', context)


def vendor_register_withgst(request):
    context = {}
    return render(request, 'vendor/register.html', context)


def vendor_verify_location(request, pk):
    context = {}
    return render(request, 'vendor/verify_location.html', context)


def vendor_add_service_location(request):
    context = {}
    return render(request, 'vendor/add_location.html', context)


def vendor_add_gst(self, pk):
    context = {}
    return render(request, 'vendor/add_gst.html', context)


def vendor_verify_gst(self, pk):
    context = {}
    return render(request, 'vendor/verify_gst.html', context)


def vendor_register_nogst(request):
    context = {}
    return render(request, 'vendor/register.html', context)


def vendor_send_otp(request, pk):
    context = {}
    return render(request, 'vendor/send_otp.html', context)


def vendor_verify_otp(request, pk):
    context = {}
    return render(request, 'vendor/verify_otp.html', context)


def vendor_add_bank_account(request, pk):
    context = {}
    return render(request, 'vendor/add_bank_account.html', context)

# Shop Views for Vendor - Product


def vendor_create_product(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Product Created Successfully")

    context = {"form": form}
    return render(request, 'vendor/create_product.html', context)


def vendor_update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes Saved Successfully")

    context = {"form": form, "product": product}
    return render(request, 'vendor/update_product.html', context)


def vendor_list_products(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'vendor/list_product.html', context)


def vendor_detail_product(request, pk):
    product = Product.objects.get(id=pk)
    pre = UserReview.objects.filter(product=product).all
    ptag = Tag.objects.filter(product=product).all

    context = {
        "product": product,
        'ptag': ptag,
        'pre': pre
        }
    return render(request, 'vendor/detail_product.html', context)

# Shop Views for Vendor - Listing


def vendor_create_listing(request):
    vendor = Vendor.objects.get(user=request.user)
    form = ListingForm(initial={'vendor': vendor})
    if request.method == 'POST':
        form = ListingForm(request.POST,
                           initial={
                               'vendor': vendor
                           })
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Listing Created')
    context = {'form': form}
    return render(request, 'vendor/create_listing.html', context)


def vendor_update_listing(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == 'POST':
        form = ListingForm(request.POST,
                           instance=listing)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Listing Updated')
    context = {'form': form}
    return render(request, 'vendor/update_listing.html', context)


def vendor_delete_listing(request, pk):
    listing = Listing.objects.get(id=pk)
    if not listing:
        messages.warning(request, 'No Such Listing')

    if request.method == 'POST':
        if listing:
            listing.delete()
            messages.success(request,
                             'Listing Deleted')
        else:
            messages.warning(request,
                             'No Such Listing')
    context = {'listing': listing}
    return render(request, 'vendor/delete_listing.html', context)


def vendor_list_listings(request):
    listings = Listing.objects.all()
    context = {'listings': listings}
    return render(request, 'vendor/list_listing.html', context)


def vendor_detail_listing(request, pk):
    listing = Listing.objects.get(id=pk)
    vendor = Vendor.objects.get(id=listing.vendor)
    product = Product.objects.get(id=listing.product)

    context = {'listing': listing, 'vendor': vendor,
               'product': product}

    return render(request, 'vendor/detail_listing.html', context)


def vendor_create_location(request):
    form = DeliveryLocationForm()

    if request.method == 'POST':
        form = DeliveryLocationForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Service Location Added Successfully")

    context = {"form": form}
    return render(request, 'vendor/create_location.html', context)


def vendor_update_location(request, pk):
    location = DeliveryLocation.objects.get(id=pk)
    form = DeliveryLocationForm(instance=location)

    if request.method == 'POST':
        form = DeliveryLocationForm(request.POST, instance=location)
        if form.is_valid:
            location = form.save()
            messages.success(request, "Changes To Service Location Successful")

    context = {"form": form, 'sl': location}
    return render(request, 'vendor/update_location.html', context)


def vendor_list_locations(request):
    locations = DeliveryLocation.objects.all()
    context = {'locations': locations}
    return render(request, 'vendor/list_location.html', context)


def vendor_detail_location(request, pk):
    location = DeliveryLocation.objects.get(pk)
    context = {'location': location}
    return render(request, 'vendor/detail_location.html', context)


def vendor_list_orders(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'vendor/list_order.html', context)


def vendor_detail_order(request, pk):
    order = Order.objects.get(id=pk)
    products = order.get_cart_items()
    cart_total = order.get_cart_total()
    commission = order.get_total_commission()
    context = {
        'order': order,
        'products': products,
        'cart_total': cart_total,
        'commission': commission

    }
    return render(request, 'vendor/detail_order.html', context)


def vendor_list_payments(request):
    payments = Payment.objects.all()
    context = {'payments': payments}
    return render(request, 'vendor/list_payment.html', context)


def vendor_detail_payment(request, pk):
    payment = Payment.objects.get(id=pk)
    context = {'payment': payment}
    return render(request, 'vendor/detail_payment.html', context)


def vendor_create_support_message(request):
    vendor = Vendor.objects.get(user=request.user)
    form = SupportMessageForm(initial={'vendor': vendor})

    if request.method == 'POST':
        form = SupportMessageForm(request.POST,
                                  initial={
                                      'vendor': vendor,
                                  })
        if form.is_valid():
            form.save()
            messages.success(request, "Message Created")
    context = {'form': form}
    return render(request, 'vendor/create_support_message.html', context)


def vendor_update_support_message(request, pk):
    vendor = Vendor.objects.get(user=request.user)
    message = SupportMessage.objects.get(id=pk)
    form = SupportMessageForm(initial={'vendor': vendor}, instance=message)

    if request.method == 'POST':
        form = SupportMessageForm(
            request.POST,
            initial={'vendor': vendor},
            instance=message,)
        messages.success(request, "Message Updated")

    context = {'form': form}
    return render(request, 'vendor/update_support_message.html', context)


def vendor_delete_support_message(request, pk):
    item = SupportMessage.objects.get(id=pk)

    if not item:
        messages.warning(request, "No Such Message")

    if request.method == 'POST':
        if item:
            item.delete()
            messages.success(request, "Message Deleted")
        else:
            messages.warning(request, "No Such Message")
    context = {'item': item}
    return render(request, 'vendor/delete_support_message.html', context)


def vendor_list_support_messages(request):
    message = SupportMessage.objects.all()
    context = {'messages': message}
    return render(request, 'vendor/list_support_message.html', context)


def vendor_detail_support_message(request, pk):
    message = SupportMessage.objects.get(id=pk)
    context = {'message': message}
    return render(request, 'vendor/detail_support_message.html', context)


def vendor_list_reports(request):
    reports = SaleReport.objects.all()
    context = {'reports': reports}
    return render(request, 'vendor/add_support_message.html', context)


def vendor_detail_report(request, pk):
    report = SaleReport.objects.get(id=pk)
    vendor = Vendor.objects.get(id=report.vendor)
    order = Order.objects.get(id=report.order)
    products = order.get_cart_items()

    context = {
        'report': report,
        'vendor': vendor,
        'order': order,
        'products': products,
    }
    return render(request, 'vendor/add_support_message.html', context)
