from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=50, default='')
    client = models.CharField(max_length=20, default='')
    application = models.CharField(max_length=10,  default='')
    type = models.CharField(max_length=20, default='')
    category = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=200, default='')
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def pub_date_short(self):
        return self.pub_date.strftime('%b %e %Y')

class Step(models.Model):
    title = models.CharField(max_length=50, default='')
    step_num = models.IntegerField(default=1)
    step_nav = models.CharField(max_length=250, default='')
    step_text = models.TextField()
    step_note = models.TextField()
    step_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
