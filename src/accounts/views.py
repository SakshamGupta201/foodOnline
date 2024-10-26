from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm


class SignUpView(CreateView):
    template_name = "accounts/registerUser.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "accounts/login.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
