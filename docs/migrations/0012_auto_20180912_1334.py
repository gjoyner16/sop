# Generated by Django 2.0 on 2018-09-12 17:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0011_auto_20180912_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='step',
            name='step_num',
            field=models.IntegerField(default=1, verbose_name='step'),
        ),
    ]