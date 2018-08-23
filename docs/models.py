from django.db import models
from django.contrib.auth.models import User

class ClientFolder(models.Model):
    client = models.CharField(max_length=100, default='')

class CategoryFolder(models.Model):
    client = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=100, default='')

class Document(models.Model):
    title = models.CharField(max_length=50, default='')
    application = models.CharField(max_length=10,  default='')
    type = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=200, default='')
    pub_date = models.DateTimeField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    client = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=100, default='')

    def pub_date_short(self):
        return self.pub_date.strftime('%b %e %Y')

class Step(models.Model):
    title = models.CharField(max_length=50, default='')
    step_num = models.FloatField(default=1)
    step_nav = models.CharField(max_length=250, default='')
    step_text = models.TextField()
    step_note = models.TextField()
    step_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
