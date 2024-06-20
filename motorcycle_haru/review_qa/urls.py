from django.urls import path

from .views import AddReviewView


app_name = 'review_qa'

urlpatterns = [
    path('<int:bike_id>/add_review', AddReviewView.as_view(), name='add_review'),
]
