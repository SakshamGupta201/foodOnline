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
    forgot_password_view,
    reset_password_validate,
    reset_password,
)


urlpatterns = [
    path("", account_view, name="myAccount"),
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_vendor_view, name="vendor_register"),
    path("customerDashboard/", customer_dashboard_view, name="customerDashboard"),
    path("vendorDashboard/", vendor_dashboard_view, name="vendorDashboard"),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
    path("forgot-password/", forgot_password_view, name="forgot_password"),
    path(
        "reset-password-validate/<uidb64>/<token>/",
        reset_password_validate,
        name="reset_password_validate",
    ),
    path("reset-password/", reset_password, name="reset_password"),
]
