# Generated by Django 4.1.5 on 2023-04-16 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_alter_usertransactions_w_gas_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertransactions',
            name='w_gas_fee',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
