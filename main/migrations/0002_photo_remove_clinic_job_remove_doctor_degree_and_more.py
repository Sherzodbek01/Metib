# Generated by Django 4.1.7 on 2023-08-21 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Clinic/')),
            ],
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='job',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='job',
        ),
        migrations.RemoveField(
            model_name='header',
            name='private_office',
        ),
        migrations.AddField(
            model_name='doctor',
            name='number',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='header',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='header',
            name='logo',
            field=models.ImageField(default=1, upload_to='Logo/'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='clinic',
            name='photo',
        ),
        migrations.DeleteModel(
            name='Degree',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.DeleteModel(
            name='Private_office',
        ),
        migrations.AddField(
            model_name='clinic',
            name='photo',
            field=models.ManyToManyField(to='main.photo'),
        ),
    ]
