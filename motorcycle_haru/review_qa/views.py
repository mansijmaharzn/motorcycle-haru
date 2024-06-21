from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from bikes.models import Bike
from .models import Review, Question, Answer
from .forms import NewReviewForm, NewQuestionForm, NewAnswerForm


class AddReviewView(View):
    def post(self, request, bike_id):
        bike = get_object_or_404(Bike, pk=bike_id)
        form = NewReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.bike = bike
            review.author = request.user
            review.save()

            response = {
                'status': 'success',
                'message': 'Review added successfully',
                'review': {
                    'content': review.content,
                    'rating': review.get_rating_display(),
                    'author': review.author.username,
                    'date_posted': review.date_posted.strftime('%Y-%m-%d %H:%M:%S')
                }
            }

        else:
            response = {
                'status': 'error',
                'message': 'There was an error with your submission.',
                'errors': form.errors
            }
        
        return JsonResponse(response)
    

class AddQuestionView(View):
    def post(self, request, bike_id):
        bike = get_object_or_404(Bike, pk=bike_id)
        form = NewQuestionForm(request.POST)

        if form.is_valid():
            question = form.save(commit=False)
            question.bike = bike
            question.author = request.user
            question.save()

            response = {
                'status': 'success',
                'message': 'Question added successfully',
                'question': {
                    'content': question.content,
                    'author': question.author.username,
                    'date_posted': question.date_posted.strftime('%Y-%m-%d %H:%M:%S')
                }
            }

        else:
            response = {
                'status': 'error',
                'message': 'There was an error with your submission.',
                'errors': form.errors
            }
        
        return JsonResponse(response)
    

class AddAnswerView(View):
    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        form = NewAnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()

            response = {
                'status': 'success',
                'message': 'Answer added successfully',
                'answer': {
                    'content': answer.content,
                    'author': answer.author.username,
                    'date_posted': answer.date_posted.strftime('%Y-%m-%d %H:%M:%S')
                }
            }

        else:
            response = {
                'status': 'error',
                'message': 'There was an error with your submission.',
                'errors': form.errors
            }
        
        return JsonResponse(response)


class ReviewView(View):
    def get(self, request, review_id):
        review = get_object_or_404(Review, pk=review_id)

        return render(request, 'review_qa/review.html', {
            'review': review
        })


class QuestionView(View):
    def get(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        answers = Answer.objects.filter(question=question)
        answer_form = NewAnswerForm

        return render(request, 'review_qa/question_answer.html', {
            'question': question,
            'answers': answers,
            'answer_form': answer_form
        })