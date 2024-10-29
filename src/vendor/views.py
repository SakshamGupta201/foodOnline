from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from accounts.models import CustomUser


@login_required
def vendor_profile(request):
    return render(request, "vendor/vendor_profile.html")
