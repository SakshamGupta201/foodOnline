from django.contrib import admin

from accounts.models import CustomUser, UserProfile


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "username", "role", "is_active")
    ordering = ("-date_joined",)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["password"]
        return self.readonly_fields


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
