# Generated by Django 2.2.2 on 2019-06-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='order_id',
            field=models.IntegerField(max_length=10),
        ),
    ]
