# Generated by Django 3.1.7 on 2021-06-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20210628_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalentity',
            name='kind',
            field=models.CharField(choices=[(0, 'Person'), (1, 'Company')], default=0, max_length=7),
        ),
    ]
