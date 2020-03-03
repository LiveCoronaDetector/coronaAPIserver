from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=50)
    confirmator = models.IntegerField()
    dead = models.IntegerField()

    def __str__(self):
        return self.name