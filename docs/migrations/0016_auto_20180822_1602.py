# Generated by Django 2.0 on 2018-08-22 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0015_auto_20180822_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
