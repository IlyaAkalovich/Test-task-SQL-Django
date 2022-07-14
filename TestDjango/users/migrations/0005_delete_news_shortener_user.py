# Generated by Django 4.0.2 on 2022-07-14 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_news_delete_history'),
    ]

    operations = [
        migrations.DeleteModel(
            name='News',
        ),
        migrations.AddField(
            model_name='shortener',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]