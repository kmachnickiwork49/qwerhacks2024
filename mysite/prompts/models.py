from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text

class Response(models.Model):
    response_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date submitted")
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.response_text
