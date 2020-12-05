from django.db import models


class GingerHouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name
