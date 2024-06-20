from django import forms

from .models import Review


class NewReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'content',)

        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border',
                'rows': 3,
            }),
            'rating': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border',
            }),
        }