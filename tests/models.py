from django.db import models
import reprlib


class Test(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        repr1 = reprlib.Repr()
        repr1.maxstring = 100
        return "Test: '{0}' \n Description: {1}".format(self.name, repr1.repr(self.description))


class Question(models.Model):
    text = models.CharField(max_length=300)
    tests = models.ManyToManyField(Test)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=300)
    score = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text


class Result(models.Model):
    text = models.CharField(max_length=350)
    max_score = models.IntegerField('score obtained')
    tests = models.ManyToManyField(Test)

    def __str__(self):
        return self.text + '\n' + 'Score: {0}'.format(self.max_score)
