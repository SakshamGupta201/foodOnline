from django.shortcuts import render

from django.views.generic import CreateView
from accounts.forms import CustomUserCreationForm, LoginForm


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reversed("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


class LoginView(CreateView):
    template_name = "registration/login.html"
    form_class = LoginForm
    success_url = reversed("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
