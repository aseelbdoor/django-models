from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

# Create your models here.
class Snacks(models.Model):
    name= models.CharField(max_length=64,help_text="Snacks Name")
    purchaser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description=models.TextField(default="no desc available")