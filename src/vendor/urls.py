from vendor import views
from django.urls import path
from accounts import views as accounts_views
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = [
    path(
        "",
        RedirectView.as_view(url=reverse_lazy("vendorDashboard")),
        name="vendor_redirect",
    ),
    path("vendor_profile/", views.vendor_profile, name="vendor_profile"),
]
