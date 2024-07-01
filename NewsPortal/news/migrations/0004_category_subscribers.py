# Generated by Django 5.0.6 on 2024-07-01 14:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_caregory_sb_subscribe_category_sb'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(related_name='categories', through='news.Subscribe', to=settings.AUTH_USER_MODEL),
        ),
    ]