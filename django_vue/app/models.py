from django.db import models

# Create your models here.

class BadmintonInfo(models.Model):
    occupied = models.CharField(max_length=100,null=True)
    nums = models.CharField(max_length=100)

    def __str__(self):
        return str(self.occupied) + " " + str(self.nums)