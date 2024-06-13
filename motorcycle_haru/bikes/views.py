from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404

from .models import Bike, Brand, Category


class DetailView(View):
    def get(self, request, pk):
        bike = get_object_or_404(Bike, pk=pk)

        related_bikes = Bike.objects.filter(category=bike.category).exclude(pk=pk)[:3]
        return render(request, "bikes/detail.html", {
            'bike': bike,
            'related_bikes': related_bikes
        })