# Generated by Django 2.0.6 on 2018-08-23 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_announcements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='postdate',
            field=models.DateTimeField(default=''),
        ),
    ]
