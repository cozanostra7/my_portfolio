# Generated by Django 4.2.3 on 2025-02-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.tags'),
        ),
    ]
