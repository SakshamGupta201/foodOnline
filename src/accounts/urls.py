from django.urls import path
from accounts.views import SignUpView, LoginView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
