from django.db import models

# Create your models here.

class add_money(models.Model):
    for_what=models.CharField(max_length=255)
    how_much=models.IntegerField()

    def __str__(self):
        return f"{self.for_what} - {self.how_much}"