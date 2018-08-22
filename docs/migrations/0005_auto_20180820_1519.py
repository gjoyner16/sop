# Generated by Django 2.0 on 2018-08-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0004_auto_20180820_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='category',
            field=models.CharField(choices=[('inventory', 'Inventory'), ('picking', 'Picking'), ('shipping', 'Shipping'), ('receiving', 'Receiving')], default='inventory', max_length=20),
        ),
        migrations.AddField(
            model_name='document',
            name='client',
            field=models.CharField(choices=[('def', 'Default Client'), ('polaris', 'Polaris')], default='def', max_length=20),
        ),
    ]
