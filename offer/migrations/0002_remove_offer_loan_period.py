# Generated by Django 3.2.16 on 2022-12-22 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='loan_period',
        ),
    ]
