from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy as _
from django.views.generic import CreateView
from .forms import VendorForm


def vendor_home(request):
    return HttpResponse("Vendor Home Page")


class RegisterVendor(CreateView):
    form_class = VendorForm
    template_name = "vendor/register.html"
    success_url = _("vendor:vendor_home")

    def form_valid(self, form):
        form.save(request=self.request)
        return super().form_valid(form)
