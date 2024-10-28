from django.urls import path
from accounts.views import (
    signup_view,
    register_vendor_view,
    login_view,
    logout_view,
    account_view,
    customer_dashboard_view,
    vendor_dashboard_view,
    activate,
)

urlpatterns = [
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_vendor_view, name="vendor_register"),
    path("myAccount/", account_view, name="myAccount"),
    path("customerDashboard/", customer_dashboard_view, name="customerDashboard"),
    path("vendorDashboard/", vendor_dashboard_view, name="vendorDashboard"),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
]
