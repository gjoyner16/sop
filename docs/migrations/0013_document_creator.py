# Generated by Django 2.0 on 2018-08-22 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('docs', '0012_auto_20180822_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='creator',
            field=models.ForeignKey(default='NONE', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]