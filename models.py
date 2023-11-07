from django.db import models
class product_data(models.Model):
    id = models.IntegerField(max_length = 10)
    url = models.URLField(blank = True,null = True)
# Create your models here.
