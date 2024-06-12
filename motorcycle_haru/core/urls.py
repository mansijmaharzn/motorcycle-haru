from django.urls import path
from django.contrib.auth.views import LoginView

from .views import SignUpFormView, IndexView, LogoutView
from .forms import LoginForm

app_name = "core"


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("signup/", SignUpFormView.as_view(), name="signup"),
    path("login/", LoginView.as_view(template_name="core/login.html", authentication_form=LoginForm), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]