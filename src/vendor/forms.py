from typing import Any
from django import forms

from vendor.models import Vendor


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ["name", "license"]

    def __init__(self, *args, **kwargs):
        super(VendorForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        self.fields["license"].widget.attrs.update({"class": "form-control"})
        self.fields["name"].label = "Restaurant Name"
