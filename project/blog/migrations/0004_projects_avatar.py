# Generated by Django 4.2.3 on 2025-02-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='avatar',
            field=models.ImageField(blank=True, default='images/my_photo.png', null=True, upload_to='images/'),
        ),
    ]
