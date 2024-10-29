from django.db import models
from django.conf import settings
from accounts.models import UserProfile

from accounts.utils import send_email


class Vendor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    license = models.ImageField(upload_to="vendor/licenses/")
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is not None:
            vendor = Vendor.objects.get(pk=self.pk)
            if vendor.is_approved != self.is_approved:
                mail_template = "accounts/email/admin_approval_email.html"
                context = {
                    "user": self.user,
                    "is_approved": self.is_approved,
                }
                if self.is_approved:
                    mail_subject = (
                        "Congratulations! Your vendor account has been approved."
                    )

                    send_email(vendor.user.email, mail_subject, mail_template, context)
                else:
                    mail_subject = "Sorry! Your vendor account has been rejected."
                    send_email(vendor.user.email, mail_subject, mail_template, context)

        super().save(*args, **kwargs)
