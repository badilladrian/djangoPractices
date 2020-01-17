from django.db import models
from datetime import datetime

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Posts"
        
def __str__(self):
    return self.title

