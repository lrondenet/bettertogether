from django.db import models
from django.contrib.auth.models import User

# White board
class WhiteBoard(models.Model):
    subject = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
