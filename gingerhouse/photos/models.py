from django.db import models


class Photo(models.Model):
    house = models.ForeignKey("houses.GingerHouse", null=True, blank=False, on_delete=models.SET_NULL)
    image = models.ImageField(
        verbose_name="Ginger house image",
        upload_to='uploads/',
        max_length=255,
        blank=True,
        null=True,
        help_text="Ginger house image. Horizontal format, cropped to 812x680 px.",
    )
    is_primary = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ("house__id", "is_primary")

    def __str__(self):
        return self.description
