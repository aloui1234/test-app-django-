from django.db import models

class Label(models.Model):
    title = models.CharField(max_length=100)

class Annotation(models.Model):
    start = models.IntegerField()
    end = models.IntegerField()
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    text = models.TextField()
    
class Document(models.Model):
    content = models.TextField()