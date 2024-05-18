# Generated by Django 3.2.25 on 2024-05-17 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shadiusers', '0016_subscribe_createdat'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shadiusers.user')),
                ('viewed_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewed_profiles', to='shadiusers.user')),
            ],
        ),
    ]
