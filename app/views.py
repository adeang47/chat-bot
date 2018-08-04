from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from app.forms import QuestionChangeForm
from app.models import Question, QuestionChange


# Root view
class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get(self, request):
        form = QuestionChangeForm()
        questions = Question.objects.filter()
        return render(request, self.template_name, {'questions': questions, 'form': form})


    def post(self, request):
        form = QuestionChangeForm(request.POST)

        if form.is_valid():
            question_change = form.save(commit=False)
            question_change.save()
            question_change.update_question_text() # update primary question's current text

            return redirect('questionChangesView', question_id=question_change.question_id)
        else:
            form = QuestionChangeForm()
        return render(request, 'app/index.html', {'form': form})


# Display the changes to a Question over time
class QuestionChangesView(TemplateView):
    template_name = 'app/questionChanges.html'

    def get(self, request, question_id):
        question_changes = QuestionChange.objects.filter(question_id = question_id)
        return render(request, self.template_name, {'question_changes': question_changes})

