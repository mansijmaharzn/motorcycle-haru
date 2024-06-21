from django.urls import path

from .views import AddReviewView, AddQuestionView


app_name = 'review_qa'

urlpatterns = [
    path('<int:bike_id>/add_review', AddReviewView.as_view(), name='add_review'),
    path('<int:bike_id>/add_question', AddQuestionView.as_view(), name='add_question'),
]
