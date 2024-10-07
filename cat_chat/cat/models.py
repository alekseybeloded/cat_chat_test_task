from django.contrib.auth.models import User
from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    breed = models.CharField(max_length=100)
    hairiness = models.CharField(max_length=100)
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
