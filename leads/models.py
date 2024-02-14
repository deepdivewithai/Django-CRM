from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Agent(AbstractUser):
    pass

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveBigIntegerField(default=0)
    email = models.EmailField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.first_name
    