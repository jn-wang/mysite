from django.db import models

#

class XB(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    videourl = models.CharField(max_length=500)
    photourl = models.CharField(max_length=500)
    def __str__(self):
        return self.name

