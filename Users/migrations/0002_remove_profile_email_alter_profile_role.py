# Generated by Django 4.1.3 on 2022-11-27 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(default='Customer', max_length=6),
        ),
    ]