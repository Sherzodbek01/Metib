# Generated by Django 4.1.7 on 2023-08-21 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_photo_remove_clinic_job_remove_doctor_degree_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='service',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]