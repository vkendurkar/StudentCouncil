# Generated by Django 2.0.6 on 2018-08-29 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_suggestions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestions',
            name='mobno',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='suggestions',
            name='rollno',
            field=models.IntegerField(default=''),
        ),
    ]
