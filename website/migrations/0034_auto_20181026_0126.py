# Generated by Django 2.0.6 on 2018-10-25 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0033_auto_20181026_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developers',
            name='department',
            field=models.CharField(default='', max_length=250),
        ),
    ]
