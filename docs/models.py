from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class Client(models.Model):
    name = models.CharField(max_length=100, default='')
    icon = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
       return '%s' % self.name

    def get_absolute_url(self):
        return reverse('client_detail', kwargs={"pk":self.pk,})

class Category(models.Model):
    name = models.CharField(max_length=100, default='')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='categories')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return  '%s' % self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={"pk":self.pk, "client_id":self.client.id,})

class Document(models.Model):
    name = models.CharField(max_length=50, default='')
    application = models.CharField(max_length=10,  default='')
    version = models.CharField(max_length=10, default='')
    type = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=200, default='')
    pub_date = models.DateTimeField(verbose_name="date published", default=timezone.now)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='documents')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='documents')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
       return '%s' % self.name

    def pub_date_short(self):
        return self.pub_date.strftime('%b %e %Y')

    def get_absolute_url(self):
        return reverse('document_detail', kwargs={"pk":self.pk, "category_id":self.category.id, "client_id":self.client.id,})

class Step(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, default='', related_name='steps')
    step_num = models.IntegerField(verbose_name="step", default=1)
    text = models.TextField()
    note = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        ordering = ['step_num']

    def __str__(self):
        return self.step_num

    def get_absolute_url(self):
        return reverse('document_detail', kwargs={"pk":self.document.id, "category_id":self.document.category.id, "client_id":self.document.client.id,})
