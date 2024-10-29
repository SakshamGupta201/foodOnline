from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings

from accounts.models import CustomUser


def detect_user(user: CustomUser) -> str:
    if user.role == CustomUser.CUSTOMER:
        return "customerDashboard"
    elif user.role == CustomUser.VENDOR:
        return "vendorDashboard"
    elif user.role is None and user.is_superadmin:
        return "admin"


def send_email(subject: str, template_name: str, context: dict, to_email: str) -> None:
    from_email = settings.DEFAULT_FROM_EMAIL
    message = render_to_string(template_name, context)
    mail = EmailMessage(subject, message, from_email, to=[to_email])
    mail.content_subtype = "html"
    mail.send()


def send_email_verification(request, user: CustomUser) -> None:
    current_site = get_current_site(request)
    subject = "Email Verification"
    context = {
        "user": user,
        "domain": current_site.domain,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": default_token_generator.make_token(user),
    }
    send_email(subject, "accounts/email/email_verification.html", context, user.email)


def send_reset_password_email(request, user: CustomUser) -> None:
    current_site = get_current_site(request)
    subject = "Reset Password"
    context = {
        "user": user,
        "domain": current_site.domain,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": default_token_generator.make_token(user),
    }
    send_email(subject, "accounts/email/reset_password.html", context, user.email)
