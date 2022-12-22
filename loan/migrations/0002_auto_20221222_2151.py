# Generated by Django 3.2.16 on 2022-12-22 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='loan_period',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.CharField(choices=[('OPEN', 'OPEN'), ('FUNDED', 'FUNDED')], default='OPEN', max_length=50),
        ),
    ]
