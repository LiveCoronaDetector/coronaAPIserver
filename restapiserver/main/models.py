from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=50)
    confirmator = models.IntegerField()
    dead = models.IntegerField()
    modifiedDate = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name