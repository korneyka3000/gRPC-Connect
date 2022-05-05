from django.db import models


class Jobs(models.Model):
    title = models.CharField(max_length=100)
    level = models.CharField(max_length=30)
    salary = models.DecimalField(max_digits=5, decimal_places=0)
    location = models.CharField(max_length=100)


class Question(models.Model):
    body = models.CharField(max_length=150)
