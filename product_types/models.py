from django.db import models
from django.utils.text import slugify
# Create your models here.

class Type(models.Model):
    title = models.CharField(unique=True, max_length=150, null=False, blank=False)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
