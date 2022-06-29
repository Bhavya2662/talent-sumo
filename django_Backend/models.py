from email.headerregistry import ContentDispositionHeader
from gc import collect
from msilib.schema import Class
from django.db import models

# Create your models here.

# Creating new database Child_scores.
class chlid_scores_db(models.Model):
    candidate_id = models.IntegerField(max_length=100)
    candidate_name = models.CharField(max_length=100)
    access_id = models.IntegerField(max_length=100)
    Question_No = models.IntegerField(max_length=100)
    Likeability = models.IntegerField(max_length=100)
    Charm = models.CharField(max_length=100)
    Confidence = models.IntegerField(max_length=100)
    Fluency = models.IntegerField(max_length=100)
    Content = models.CharField(max_length=100)
    Overall = models.IntegerField(max_length=100)
    