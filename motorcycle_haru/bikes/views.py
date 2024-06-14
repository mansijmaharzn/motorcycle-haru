from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Bike, Brand, Category
from .forms import NewBikeForm, EditBikeForm


class BikeView(View):
    def get(self, request):
        bikes = Bike.objects.all()

        return render(request, "bikes/bikes.html", {
            'bikes': bikes
        })


class DetailView(View):
    def get(self, request, pk):
        bike = get_object_or_404(Bike, pk=pk)
        related_bikes = Bike.objects.filter(category=bike.category).exclude(pk=pk)[:3]
        
        return render(request, "bikes/detail.html", {
            'bike': bike,
            'related_bikes': related_bikes
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