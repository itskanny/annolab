# Generated by Django 3.2.12 on 2022-05-18 16:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_auto_20220424_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
