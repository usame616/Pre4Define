from django.db import models
from django.contrib.auth.models import User





class Define(models.Model):
    word = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    pegi = models.PositiveIntegerField()
    commentCount = models.FloatField()
    commentScore = models.FloatField()
    appSizeMb = models.FloatField()
    downloads = models.PositiveBigIntegerField()
    ranking = models.PositiveIntegerField

def __str__(self):
    return self.word + '' + self.ranking
