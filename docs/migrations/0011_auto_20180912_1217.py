# Generated by Django 2.0 on 2018-09-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0010_auto_20180912_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='step',
            name='step_num',
            field=models.IntegerField(default=1),
        ),
    ]