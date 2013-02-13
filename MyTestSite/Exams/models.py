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


class Answers(models.Model):
    userID = models.IntegerField()
    questionID = models.ForeignKey(Questions)
    answer = models.CharField(max_length=254)
