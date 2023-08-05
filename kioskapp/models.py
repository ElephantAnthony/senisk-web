from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Kiosk(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='kiosk')
    ui = models.IntegerField(null=False)
    type = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=20, null=False)
    mainColor = models.CharField(max_length=20, null=True)
    subColor = models.CharField(max_length=20, null=True)