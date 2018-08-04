from django.test import TestCase

from app.models import Topic, Question, QuestionChange


class QuestionTest (TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name='Questions')

    def test_question_current_text_on_creation(self):
        question = Question.objects.create(original_text='This is a question?', topic=self.topic)
        self.assertEquals(question.original_text, question.current_text)



class QuestionChangeTest (TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name='Questions')
        self.question = Question.objects.create(original_text='This is a new question?', topic=self.topic)

    def test_question_change_affects_question_current_text(self):
        question_change = QuestionChange.objects.create(question=self.question, text='The question has changed?')

        self.assertEquals(self.question.current_text, question_change.text)
