# Generated by Django 5.1.3 on 2024-11-25 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartoon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartoon',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
