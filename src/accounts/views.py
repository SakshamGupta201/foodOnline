from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages

from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm, VendorForm
from accounts.forms import CustomAuthenticationForm
from accounts.models import CustomUser, UserProfile
from accounts.utils import detect_user
from typing import Any


# Restrict customer to access vendor dashboard
def check_role_vendor(user):
    if user.role == CustomUser.VENDOR:
        return True
    raise PermissionDenied("You are not allowed to access this page")


# Restrict vendor to access customer dashboard
def check_role_customer(user):
    if user.role == CustomUser.CUSTOMER:
        return True
    raise PermissionDenied("You are not allowed to access this page")


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save(request=request, commit=True)
            return HttpResponseRedirect(reverse("login"))
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/registerUser.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy("home"))
        else:
            return render(request, "accounts/login.html", {"form": form})
    else:
        form = CustomAuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register_vendor_view(request):
    if request.user.is_authenticated:
        return redirect("vendor:vendor_dashboard")
    else:
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

                return redirect("vendor:vendor_dashboard")
        else:
            vendor_form = VendorForm()
            user_form = CustomUserCreationForm()

        context = {"vendor_form": vendor_form, "user_form": user_form}
        return render(request, "vendor/register.html", context)


@login_required
def account_view(request):
    user = request.user
    redirect_url = detect_user(user)
    return HttpResponseRedirect(reverse(redirect_url))


@login_required
@user_passes_test(check_role_customer)
def customer_dashboard_view(request):
    return render(request, "dashboard/customerDashboard.html")


@login_required
@user_passes_test(check_role_vendor)
def vendor_dashboard_view(request):
    return render(request, "dashboard/vendorDashboard.html")


def activate(request: Any, uidb64: str, token: str) -> Any:
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Account activated successfully")
            login(request, user)
            return redirect("myAccount")
        else:
            messages.error(request, "Activation link has expired")
            return redirect("home")
    except Exception as e:
        user = None
        messages.error(request, "Activation link has expired")
        return redirect("register")
