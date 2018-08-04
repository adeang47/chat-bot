from django import forms

from app.models import QuestionChange


# Create a new QuestionChange object
class QuestionChangeForm(forms.ModelForm):
    class Meta:
        model = QuestionChange
        fields = ['question', 'text']
