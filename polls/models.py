from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    questions = models.ManyToManyField('Question')
    user = models.ForeignKey('auth.User')


class Question(models.Model):
    question_text = models.CharField(max_length=200)


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    choice_multiple = models.CharField(max_length=200)
    choice_boolean = models.Boolean()

