from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pob_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.question_text}'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question_id}, {self.choice_text}'
