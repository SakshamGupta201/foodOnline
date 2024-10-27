from django.urls import path
from accounts.views import SignUpView, login_view, logout_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", logout_view, name="logout"),
]
