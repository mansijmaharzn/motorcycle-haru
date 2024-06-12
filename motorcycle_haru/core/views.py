from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SignUpForm


class SignUpFormView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "core/signup.html", {"form": form})
    
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")

        return render(request, "core/signup.html", {"form": form})

    def index(self, request):
        return render(request, "core/index.html")


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("/login/")
    

class IndexView(View):
    def get(self, request):
        return render(request, "core/index.html")
