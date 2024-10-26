from vendor import views
from django.urls import path

app_name = "vendor"

urlpatterns = [
    path("", views.vendor_home, name="vendor_home"),
    path("register/", views.RegisterVendor.as_view(), name="vendor_register"),
]
