# Generated by Django 2.2.1 on 2019-07-16 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gametest', '0002_ads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='index',
            field=models.IntegerField(default=0),
        ),
    ]
