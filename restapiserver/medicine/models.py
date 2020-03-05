from django.db import models

class Pharmacy(models.Model):
    pharmacy_name = models.CharField(max_length=50)
    mask = models.IntegerField()
    hand_sanitizer = models.IntegerField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    modifiedDate = models.DateTimeField(auto_now=True, blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=20)

    def __str__(self):
        return self.pharmacy_name