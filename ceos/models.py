from django.db import models


# Create your models here.
class CeosUpdate(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=40)
    year_started = models.IntegerField(null = True)

    def __str__(self):
        return self.name
