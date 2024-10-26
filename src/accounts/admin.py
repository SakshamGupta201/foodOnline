from django.contrib import admin

from accounts.models import CustomUser, UserProfile


class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "username",
        "email",
        "phone_number",
        "role",
    ]
    search_fields = [
        "first_name",
        "last_name",
        "username",
        "email",
        "phone_number",
        "role",
    ]
    list_filter = ["role"]
    readonly_fields = ["date_joined", "last_login", "password"]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
