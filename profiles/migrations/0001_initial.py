# Generated by Django 2.0.6 on 2018-07-24 10:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.CharField(max_length=8)),
                ('branch', models.CharField(choices=[('CH', 'Chemical Engineering'), ('CO', 'Computer Engineering'), ('CV', 'Civil Engineering'), ('EC', 'Electronics and Communications Engineering'), ('EE', 'Elelctrical and Electronics Engineering'), ('IT', 'Information Technology'), ('ME', 'Mechanical Engineering'), ('MN', 'Mining Engineering'), ('MT', 'Materials and Metallurgical Engineering')], max_length=2)),
                ('post', models.CharField(choices=[('PR', 'President'), ('VP', 'Vice President'), ('GS', 'General Secretary'), ('JU', 'Joint Secretary UG'), ('JP', 'Joint Secretary PG'), ('GR', "PG/PhD Girls' Representative"), ('TU', 'Technical Secretary UG'), ('TP', 'Technical Secretary PG'), ('CU', 'Cultural Secretary UG'), ('CP', 'Cultural Secretary PG'), ('EC', 'Engineer Convenor'), ('IC', 'Incident Convenor'), ('IT', 'Incident Treasurer'), ('ET', 'Engineer Treasurer'), ('EJ', 'Engineer Joint Convenor'), ('IJ', 'Incident Joint Convenor')], max_length=2)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('hostel_block', models.CharField(max_length=20)),
                ('phone_num', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '9876543210'. Up to 10 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
