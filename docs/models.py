from django.db import models
from django.contrib.auth.models import User

CLIENT_CHOICES = (
    ('def', 'Default Client'),
    ('polaris', 'Polaris')
)

APPLICATION_CHOICES = (
    ('jda','JDA/RP'),
    ('hj', 'Highjump'),
    ('sap','SAP'),
    ('o', 'Other')
)

TYPE_CHOICES = (
    ('rf','RF'),
    ('gui', 'GUI'),
    ('web','Web UI'),
)

CATEGORY_CHOICES = (
    ('inventory','Inventory'),
    ('picking', 'Picking'),
    ('shipping','Shipping'),
    ('receiving', 'Receiving')
)

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=50, default='')
    client = models.CharField(max_length=20, choices=CLIENT_CHOICES, default='def')
    application = models.CharField(max_length=3, choices=APPLICATION_CHOICES, default='jda')
    type = models.CharField(max_length=3, choices=TYPE_CHOICES, default='rf')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='inventory')
    description = models.CharField(max_length=200, default='')
    pub_date = models.DateTimeField()

    def pub_date_short(self):
        return self.pub_date.strftime('%b %e %Y')

class Step(models.Model):
    title = models.CharField(max_length=50, default='')
    step_num = models.IntegerField(default=1)
    step_nav = models.CharField(max_length=250, default='')
    step_text = models.TextField()
    step_note = models.TextField()
    step_image = models.ImageField(upload_to='images/')
