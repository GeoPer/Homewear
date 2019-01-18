import datetime
from django.db import models
from django.utils import timezone

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    category_description = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#sxetika me katigories

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=70)
    product_description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
