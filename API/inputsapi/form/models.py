from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Form(models.Model):
    form_text = models.CharField(max_length=200)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.form_text


class Choice(models.Model): 
    form = models.ForeignKey(Form, related_name='choices',
     on_delete=models.CASCADE) 

    choice_text = models.CharField(max_length=100)

    def __str__(self): 
        return self.choice_text


class Input(models.Model): 
    choice = models.ForeignKey(Choice, 
    related_name='inputs', 
    on_delete=models.CASCADE)

    form = models.ForeignKey(Form, 
    on_delete=models.CASCADE) 

    filled_by = models.ForeignKey(User, 
    on_delete=models.CASCADE)

    class Meta: 
        unique_together = ("form", "filled_by")



