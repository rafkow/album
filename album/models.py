from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    width = models.IntegerField(default=0, null=True, blank=True)
    height = models.IntegerField(default=0, null=True, blank=True)
    color = models.IntegerField(default=0)
    url = models.CharField(max_length=100, null=True, blank=True)
    albumId = models.IntegerField(default=0,  blank=True)


