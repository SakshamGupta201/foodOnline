from django.urls import path
from accounts.views import (
    SignUpView,
    register_vendor_view,
    login_view,
    logout_view,
    account_view,
    customer_dashboard_view,
    vendor_dashboard_view,
)

urlpatterns = [
    path("login/", login_view, name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_vendor_view, name="vendor_register"),
    path("myAccount/", account_view, name="myAccount"),
    path("customerDashboardd/", customer_dashboard_view, name="customerDashboard"),
    path("vendorDashboard/", vendor_dashboard_view, name="vendorDashboard"),
]
