# Generated by Django 3.2.12 on 2022-04-06 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='group'),
        ),
    ]
