from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    """Categories are used to limit voting and present entries in groupings"""
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class GingerHouse(models.Model):
    """GingerHouses are entries in the contest, to be voted on. Each represents
    a physical Gingerbread House that is displayed on public display in town and
    is a model of a structure in town."""
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    display_address = models.TextField(blank=True)
    model_address = models.TextField(blank=True)

    class Meta:
        ordering = ["-category__name", ]

    def __str__(self):
        return self.name

    @property
    def primary_image(self):
        image = self.photo_set.filter(is_primary=True).first()
        return image

    def get_absolute_url(self):
        return reverse("houses:detail", kwargs={"pk": self.id})


class Vote(models.Model):
    email = models.CharField(max_length=255)
    ginger_house = models.ForeignKey('GingerHouse', on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(self.email, self.ginger_house.category.name, self.ginger_house.name)
