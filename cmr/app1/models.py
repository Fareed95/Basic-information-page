from django.db import models

# Create your models here.
class INFORMATION(models.Model):
    firstname = models.CharField(max_length= 20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    Address1 = models.CharField(max_length=100)
    Address2 = models.CharField(max_length=100)
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=30)
    Pin = models.IntegerField()

    def __str__(self) -> str:
        return self.firstname


