from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from accounts.forms import CustomUserCreationForm
from accounts.models import CustomUser, UserProfile
from .forms import VendorForm


@login_required
def vendor_home(request):
    return HttpResponse("Vendor Home Page")


def RegisterVendor(request):
    if request.method == "POST":
        vendor_form = VendorForm(request.POST, request.FILES)
        user_form = CustomUserCreationForm(request.POST)
        if vendor_form.is_valid() and user_form.is_valid():
            vendor_form = vendor_form.save(commit=False)
            user_form = user_form.save(commit=False)
            user_form.role = CustomUser.VENDOR
            user_form.save()
            vendor_form.user = user_form
            user_profile = UserProfile.objects.get(user=user_form)
            vendor_form.user_profile = user_profile
            vendor_form.save()
            return redirect("vendor:vendor_home")
    else:
        vendor_form = VendorForm()
        user_form = CustomUserCreationForm()

    context = {"vendor_form": vendor_form, "user_form": user_form}
    return render(request, "vendor/register.html", context)
