from django.urls import path

from .views import AddReviewView, AddQuestionView, ReviewView, QuestionView, AddAnswerView


app_name = 'review_qa'

urlpatterns = [
    path('<int:bike_id>/add_review', AddReviewView.as_view(), name='add_review'),
    path('<int:bike_id>/add_question', AddQuestionView.as_view(), name='add_question'),
    path('<int:question_id>/add_answer', AddAnswerView.as_view(), name='add_answer'),
    path('<int:review_id>/review', ReviewView.as_view(), name='review'),
    path('<int:question_id>/question', QuestionView.as_view(), name='question'),
]
