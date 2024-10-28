from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage, message

from accounts.models import CustomUser


def detect_user(user: CustomUser) -> str:
    if user.role == CustomUser.CUSTOMER:
        return "customerDashboard"
    elif user.role == CustomUser.VENDOR:
        return "vendorDashboard"
    elif user.role == None and user.is_superadmin:
        return "admin"


def send_email_verification(request, user: CustomUser) -> None:
    current_site = get_current_site(request)
    subject = "Email Verification"
    message = render_to_string(
        "accounts/email/email_verification.html",
        {
            "user": user,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": default_token_generator.make_token(user),
        },
    )
    to_email = user.email

    mail = EmailMessage(subject, message, to=[to_email])
    mail.content_subtype = "html"
    mail.send()
