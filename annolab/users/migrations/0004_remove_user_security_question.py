# Generated by Django 3.2.12 on 2022-02-23 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_security_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='security_question',
        ),
    ]