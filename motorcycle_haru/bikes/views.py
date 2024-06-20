from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Bike, Brand, Category
from .forms import NewBikeForm, EditBikeForm
from review_qa.forms import NewReviewForm


class BikeView(View):
    def get(self, request):
        bikes = Bike.objects.all()
        categories = Category.objects.all()

        query = request.GET.get('query', '')
        category_id = request.GET.get('category', 0)

        if category_id:
            bikes = bikes.filter(category_id=category_id)

        if query:
            bikes = bikes.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query) | Q(brand__name__icontains=query))

        return render(request, "bikes/bikes.html", {
            'bikes': bikes,
            'categories': categories,
            'query': query,
            'category_id': int(category_id)
        })


class DetailView(View):
    def get(self, request, pk):
        bike = get_object_or_404(Bike, pk=pk)
        reviews = bike.review.all()
        related_bikes = Bike.objects.filter(category=bike.category).exclude(pk=pk)[:3]
        form = NewReviewForm

        return render(request, "bikes/detail.html", {
            'bike': bike,
            'reviews': reviews,
            'related_bikes': related_bikes,
            'form': form
        })
    

class NewBikeFormView(LoginRequiredMixin, View):
    form_class = NewBikeForm
    template_name = 'bikes/new_bike.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {
            'form': form
        })
    
    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            bike = form.save(commit=False)
            bike.owner = request.user
            bike.save()

            return redirect('bikes:detail', pk=bike.pk)


class EditBikeView(LoginRequiredMixin, View):
    form_class = EditBikeForm
    template_name = 'bikes/edit_bike.html'

    def get(self, request, pk):
        form = self.form_class(instance=get_object_or_404(Bike, pk=pk, owner=request.user))
        return render(request, self.template_name, {
            'form': form
        })

    def post(self, request, pk):
        form = self.form_class(request.POST, instance=get_object_or_404(Bike, pk=pk, owner=request.user))
        if form.is_valid():
            form.save()
            return redirect('bikes:detail', pk=pk)


class DeleteBikeView(LoginRequiredMixin, View):
    def get(self, request, pk):
        bike = get_object_or_404(Bike, pk=pk, owner=request.user)
        bike.delete()
        return redirect('core:index')