from typing import Any
from django import forms

from vendor.models import Vendor


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ["name", "license"]

    def save(self, request, commit: bool = True) -> Any:
        vendor = super().save(commit=False)
        vendor.user = request.user
        # ! fix the issue
        vendor.user_profile = request.user.user_profile
        if commit:
            vendor.save()
        return vendor
