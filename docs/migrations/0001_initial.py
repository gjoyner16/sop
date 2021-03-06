# Generated by Django 2.0 on 2018-09-05 22:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('application', models.CharField(default='', max_length=10)),
                ('type', models.CharField(default='', max_length=20)),
                ('description', models.CharField(default='', max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='docs.Category')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='docs.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_num', models.FloatField(default=1)),
                ('navigation', models.CharField(default='', max_length=250)),
                ('text', models.TextField()),
                ('note', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('document', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='docs.Document')),
            ],
            options={
                'ordering': ['step_num'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docs.Client'),
        ),
    ]
