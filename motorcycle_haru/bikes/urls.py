from django.urls import path

from .views import DetailView, NewBikeFormView, DeleteBikeView


app_name = "bikes"


urlpatterns = [
    path("<int:pk>/", DetailView.as_view(), name="detail"),
    path("<int:pk>/delete", DeleteBikeView.as_view(), name="delete"),
    path("new/", NewBikeFormView.as_view(), name="new"),
]