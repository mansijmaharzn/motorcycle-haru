from django import forms

from .models import Bike


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class NewBikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ('name', 'description', 'price', 'image', 'category', 'brand')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'brand': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
        }