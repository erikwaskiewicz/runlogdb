# Generated by Django 2.0.6 on 2018-07-06 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_auto_20180705_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='experiment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='input',
            name='run_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='input',
            name='samples',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
