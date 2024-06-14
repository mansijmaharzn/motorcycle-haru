from django.urls import path

from .views import DetailView, NewBikeFormView, DeleteBikeView, EditBikeView, BikeView


app_name = "bikes"


urlpatterns = [
    path('', BikeView.as_view(), name="bikes"),
    path("<int:pk>/", DetailView.as_view(), name="detail"),
    path("<int:pk>/edit", EditBikeView.as_view(), name="edit"),
    path("<int:pk>/delete", DeleteBikeView.as_view(), name="delete"),
    path("new/", NewBikeFormView.as_view(), name="new"),
]