# Generated by Django 2.0.6 on 2018-08-11 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20180724_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='MinuteOfMeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='M.O.M.s')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
