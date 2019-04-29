from django.db import models

# Create your models here.
class powerquestionbank(models.Model):
    SID = models.CharField(max_length=50)
    icontains = models.CharField(max_length=50)
    rubric = models.CharField(max_length=50)
    answer = models.CharField(max_length=500)
    option = models.CharField(max_length=500)

class Message(models.Model):
    user = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    Message = models.CharField(max_length=500)
    def __str__(self):
        return self.user