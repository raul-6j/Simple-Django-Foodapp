# Generated by Django 5.0 on 2024-01-05 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_profiles_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profilepic.png', upload_to='profile_pictures'),
        ),
    ]
