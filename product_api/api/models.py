from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    rating = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
