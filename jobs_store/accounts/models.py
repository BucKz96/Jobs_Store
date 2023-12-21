from django.db import models
from django.contrib.auth.models import User


class UserSkill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    job = models.CharField(max_length=100, blank=True)
    skills = models.ManyToManyField(UserSkill)

    def __str__(self):
        return self.user.username

