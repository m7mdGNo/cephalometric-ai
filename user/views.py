from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render

class CustomLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('upload') 
    

class CustomLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')