# Generated by Django 3.2.25 on 2024-05-15 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shadiusers', '0008_auto_20240515_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shadiusers.user'),
            preserve_default=False,
        ),
    ]