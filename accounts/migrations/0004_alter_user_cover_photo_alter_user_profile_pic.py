# Generated by Django 4.1.5 on 2023-01-21 17:41

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_cover_photo_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cover_photo',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dbbfeegje/image/upload/v1673299668/cld-sample-2.jpg', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dbbfeegje/image/upload/v1673299668/cld-sample.jpg', max_length=255, verbose_name='image'),
        ),
    ]
