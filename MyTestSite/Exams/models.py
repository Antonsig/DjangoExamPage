from django.db import models

# Create your models here.

class Exams(models.Model):
    name = models.CharField(max_length= 50)
    date_created = models.DateField(auto_now=True)
    date_opened = models.DateField()
    date_closed = models.DateField()

class Questions(models.Model):
    exam = models.ForeignKey(Exams)
    question = models.CharField(max_length=256)
    answerA = models.CharField(max_length=256)
    answerB = models.CharField(max_length=256)
    answerC = models.CharField(max_length=256)
    answerD = models.CharField(max_length=256)
    correct_answer = models.CharField(max_length=1)


class Answers(models.Model):
    userID = models.IntegerField()
    exam = models.ForeignKey(Exams)
    questionID = models.IntegerField()
    user_answer = models.CharField(max_length=1)