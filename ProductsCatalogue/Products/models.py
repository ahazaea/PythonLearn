from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class product(models.Model):
    Name = models.CharField(max_length=200)
    Image = models.ImageField(
        upload_to='products_thumbs')
    description = models.CharField(max_length=500)
