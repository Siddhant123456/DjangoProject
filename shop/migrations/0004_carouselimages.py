# Generated by Django 2.2.2 on 2019-06-19 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190619_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='shop/carousel/images')),
            ],
        ),
    ]