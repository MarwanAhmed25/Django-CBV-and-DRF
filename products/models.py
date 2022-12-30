from django.db import models
from django.utils.text import slugify
# Create your models here.
COLORS = (
    ('R','Red'),
    ('B','Blue'),
    ('G','Gray'),
)

class Product(models.Model):
    title = models.CharField(unique=True, max_length=150, null=False, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    color = models.CharField(max_length=50, choices=COLORS)
    description = models.TextField()
    stock = models.IntegerField()
    brand = models.CharField(max_length=150)
    img1 = models.ImageField(upload_to='images/')
    img2 = models.ImageField(upload_to='images/')
    img3 = models.ImageField(upload_to='images/')
    img4 = models.ImageField(upload_to='images/')
    img5 = models.ImageField(upload_to='images/')
    model_id = models.ForeignKey("product_models.BrandModel", on_delete=models.CASCADE)
    type_id = models.ForeignKey("product_types.Type", on_delete=models.CASCADE)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title