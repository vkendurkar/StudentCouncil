# Generated by Django 2.0.6 on 2018-09-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0028_announcements_eventdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='councilmess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='')),
            ],
        ),
    ]
