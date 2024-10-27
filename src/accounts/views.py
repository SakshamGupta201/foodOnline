from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm, VendorForm
from accounts.forms import CustomAuthenticationForm
from accounts.models import CustomUser, UserProfile
from accounts.utils import detect_user


class SignUpView(CreateView):
    template_name = "accounts/registerUser.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


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
def customer_dashboard_view(request):
    return render(request, "dashboard/customerDashboard.html")


@login_required
def vendor_dashboard_view(request):
    return render(request, "dashboard/vendorDashboard.html")
