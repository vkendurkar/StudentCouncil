# Generated by Django 2.0.6 on 2018-07-24 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20180724_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_pics/%Y/%m/%d'),
        ),
    ]
