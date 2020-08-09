from django.db import models
from django.contrib.auth.models import User


class Exam(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    individual_price = models.IntegerField()
    group_price = models.IntegerField()
    examiner = models.ManyToManyField(User)
    date = models.DateTimeField()
    # poster = models.ImageField()

    def __str__(self):
        return self.title
