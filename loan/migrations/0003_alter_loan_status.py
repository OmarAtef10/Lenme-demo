# Generated by Django 3.2.16 on 2022-12-23 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_auto_20221222_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.CharField(choices=[('FUNDED', 'FUNDED'), ('OPEN', 'OPEN')], default='OPEN', max_length=50),
        ),
    ]
