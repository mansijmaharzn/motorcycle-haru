from django.urls import path

from .views import DetailView


app_name = "bikes"


urlpatterns = [
    path("<int:pk>/", DetailView.as_view(), name="detail"),
]