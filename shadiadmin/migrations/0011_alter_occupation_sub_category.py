# Generated by Django 3.2.17 on 2023-02-24 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shadiadmin', '0010_rename_sub_id_occupation_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupation',
            name='sub_category',
            field=models.CharField(max_length=100),
        ),
    ]
