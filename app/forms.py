from django import forms

from app.models import QuestionChange


class QuestionChangeForm(forms.ModelForm):
    class Meta:
        model = QuestionChange
        fields = ['question', 'text']
