# Generated by Django 2.2.1 on 2019-07-16 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gametest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='ads')),
                ('desc', models.CharField(max_length=20)),
                ('index', models.ImageField(default=0, upload_to='')),
            ],
        ),
    ]