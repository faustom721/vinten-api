# Generated by Django 3.1.7 on 2021-04-18 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_buyer_externalperson_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]