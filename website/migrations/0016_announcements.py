# Generated by Django 2.0.6 on 2018-08-23 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_representatives_reppost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(default='', max_length=50)),
                ('postdate', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(default='')),
                ('contact', models.IntegerField(default='')),
            ],
        ),
    ]
