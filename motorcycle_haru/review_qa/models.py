from django.db import models
from django.contrib.auth.models import User

from bikes.models import Bike


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    content = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    bike = models.ForeignKey(Bike, related_name='review', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='review', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Review by {self.author} for {self.bike}"