# Generated by Django 4.2.3 on 2024-03-22 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='test',
        ),
    ]
