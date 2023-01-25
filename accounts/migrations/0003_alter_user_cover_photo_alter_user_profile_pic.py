# Generated by Django 4.1.5 on 2023-01-21 17:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_moredetails_user_details_alter_moredetails_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cover_photo',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dbbfeegje/image/upload/v1673299668/cld-sample-2.jpg', max_length=255, verbose_name='raw'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dbbfeegje/image/upload/v1673299668/cld-sample.jpg', max_length=255, verbose_name='raw'),
        ),
    ]
