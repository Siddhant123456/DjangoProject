# Generated by Django 2.2.2 on 2019-06-25 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20190624_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default='0 ', max_length=100),
        ),
    ]
