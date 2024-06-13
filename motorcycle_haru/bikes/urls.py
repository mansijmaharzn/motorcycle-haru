from django.urls import path

from .views import DetailView, NewBikeFormView


app_name = "bikes"


urlpatterns = [
    path("<int:pk>/", DetailView.as_view(), name="detail"),
    path("new/", NewBikeFormView.as_view(), name="new"),
]