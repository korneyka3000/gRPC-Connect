from django.db import models


LEV = [
    ('Junior', 'Junior'),
    ('Middle', 'Middle'),
    ('Senior', 'Senior'),
]


class Jobs(models.Model):
    title = models.CharField(max_length=100)
    level = models.CharField(max_length=30, choices=LEV)
    salary = models.DecimalField(max_digits=5, decimal_places=1)
    location = models.CharField(max_length=100)

