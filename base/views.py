from django.contrib.auth.models import Group
from apps.accounts.forms import CreateCustomerForm, CreateDeliveryForm
from apps.accounts.forms import CreateVendorForm, CreateUserForm
from django.shortcuts import redirect, render
from django.contrib import messages
from apps.customer.models import Customer
from apps.seller.models import Vendor
from apps.delivery.models import Delivery
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'home.html', {})


def registerAdmin(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.is_superuser = True
            user.save()
            phone = form.cleaned_data.get('phone')
            print(user, phone)
            messages.success(request,
                             f'Account Created for {user} with {phone}')
            return redirect('/')

    context = {'form': form}
    return render(request, 'register.html', context)


def registerCustomer(request):
    form = CreateCustomerForm()

    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)

        if form.is_valid():
            user = form.save()
            Group.objects.get_or_create(name="customer")
            group = Group.objects.get(name="customer")
            user.groups.add(group)
            aadhar = form.cleaned_data.get('aadhar_number')
            customer = Customer.objects.create(
                user=user, aadhar_number=aadhar, balance=0)
            customer.save()
            messages.success(request, f'{customer} saved!')
            return redirect('/')

    context = {'form': form}
    return render(request, 'register.html', context)


def registerVendor(request):
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
            return redirect('/')

    context = {'form': form}
    return render(request, 'register.html', context)


def registerDelivery(request):
    form = CreateDeliveryForm()

    if request.method == 'POST':
        form = CreateDeliveryForm(request.POST)

        if form.is_valid():
            user = form.save()
            Group.objects.get_or_create(name="delivery")
            group = Group.objects.get(name="delivery")
            user.groups.add(group)
            aadhar = form.cleaned_data.get('aadhar_number')
            delivery = Delivery.objects.create(
                user=user, aadhar_number=aadhar)
            delivery.save()
            messages.success(request, f'{delivery} saved!')
            return redirect('/')

    context = {'form': form}
    return render(request, 'register.html', context)


def user_login(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = authenticate(
            request, username=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html', {})


def logOut(request):
    logout(request)
    messages.success(request, f'{request.user} Logged Out!')
