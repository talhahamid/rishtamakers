# Generated by Django 3.2.25 on 2024-05-15 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shadiusers', '0009_personal_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
