# Generated by Django 2.0.6 on 2018-10-14 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0030_suggestions_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='developers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('department', models.TextField(default='')),
                ('mobno', models.IntegerField(default='')),
            ],
        ),
    ]
