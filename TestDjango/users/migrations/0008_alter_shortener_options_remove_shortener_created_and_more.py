# Generated by Django 4.0.2 on 2022-07-14 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_shortener_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shortener',
            options={},
        ),
        migrations.RemoveField(
            model_name='shortener',
            name='created',
        ),
        migrations.RemoveField(
            model_name='shortener',
            name='times_followed',
        ),
    ]