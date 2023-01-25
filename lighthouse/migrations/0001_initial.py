# Generated by Django 4.1.5 on 2023-01-16 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_name', models.CharField(max_length=100)),
                ('coin_address', models.CharField(max_length=200)),
                ('coin_qr_code', models.ImageField(blank=True, null=True, upload_to='')),
                ('enable', models.BooleanField(default=True)),
            ],
        ),
    ]
