# Generated by Django 3.1.7 on 2021-06-10 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20210610_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='active',
            new_name='is_active',
        ),
    ]