# Generated by Django 3.0.5 on 2020-09-04 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='mobile',
        ),
        migrations.AddField(
            model_name='customer',
            name='mobile_number',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
