from django.contrib import admin
from .models import Vendor


class VendorAdmin(admin.ModelAdmin):
    list_display = ["name", "is_approved", "created_at", "updated_at"]
    list_filter = ["is_approved", "created_at", "updated_at"]
    list_editable = ["is_approved"]
    search_fields = ["name"]


admin.site.register(Vendor, VendorAdmin)
