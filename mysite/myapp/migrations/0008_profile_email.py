# Generated by Django 2.2.6 on 2019-12-09 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20191209_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]