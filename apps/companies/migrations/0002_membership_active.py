# Generated by Django 3.1.7 on 2021-04-27 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]