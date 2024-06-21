from django import forms

from .models import Review, Question, Answer


class NewReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'content',)

        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Enter Review Here...',
                'class': 'w-full py-4 px-6 rounded-xl border',
                'rows': 3,
            }),
            'rating': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border',
            }),
        }


class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('content',)

        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Enter Question Here...',
                'class': 'w-full py-4 px-6 rounded-xl border',
                'rows': 2,
            }),
        }


class NewAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('content',)

        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Enter Answer Here...',
                'class': 'w-full py-4 px-6 rounded-xl border',
                'rows': 2,
            }),
        }
