# Generated by Django 2.2.2 on 2019-07-17 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
