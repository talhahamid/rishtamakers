# Generated by Django 4.1.7 on 2023-03-04 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shadiusers', '0004_alter_personal_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='users11',
            name='confirm_password',
            field=models.CharField(default=10, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users11',
            name='password',
            field=models.CharField(default=10, max_length=100),
            preserve_default=False,
        ),
    ]