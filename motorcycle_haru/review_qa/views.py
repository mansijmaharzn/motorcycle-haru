from django.views import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from bikes.models import Bike
from .forms import NewReviewForm


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