from django.db import models

# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0.00)

    def __str__(self):
        return self.title