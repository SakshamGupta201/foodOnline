from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from accounts.models import CustomUser


@login_required
def vendor_home(request):
    return HttpResponse("Vendor Home Page")
