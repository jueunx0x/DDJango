from django.db import models
import pymongo
class Locations(models.Model):
    num=models.CharField(max_length=70)
    gu=models.CharField(max_length=70)
    detail=models.CharField(max_length=80)

    def __str__(self):
        return self.detail