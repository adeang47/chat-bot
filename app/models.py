from django.db import models
from django.utils import timezone

from users.models import User


# Topic of a question
class Topic(models.Model):
    name = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


# Mapping of topics to create a graph-like structure
class TopicMap(models.Model):
    parent_topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='parent_topic')
    sub_topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='sub_topic')


class QuestionManager(models.Manager):
    def create(self, *args, **kwargs):
        kwargs['current_text'] = kwargs['original_text']
        return super(QuestionManager, self).create(*args, **kwargs)


# Root Question, which is displayed to Users to adjust
class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # related topic
    original_text = models.CharField(max_length=4000) # the original text from object creation
    current_text = models.CharField(max_length=4000) # show the latest text from a QuestionChange
    create_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)
    objects = QuestionManager()

    def __str__(self):
        return self.current_text


class QuestionChangeManager(models.Manager):
    def create(self, *args, **kwargs):
        q = kwargs['question']
        q.current_text = kwargs['text'] # set the related Question current text to the text of this object
        q.save()
        return super(QuestionChangeManager, self).create(*args, **kwargs)


# Mark the changes that have been made to the text of a question
class QuestionChange(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=4000)
    create_date = models.DateTimeField(default=timezone.now)
    objects = QuestionChangeManager()

    def __str__(self):
        return self.text

    def update_question_text(self):
        self.question.current_text = self.text
        self.question.save()


# User responses to a question
class QuestionResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=4000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=4000)

    def __str__(self):
        return self.text
