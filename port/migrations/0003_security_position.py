# Generated by Django 2.2.5 on 2019-09-08 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0002_security_asset'),
    ]

    operations = [
        migrations.AddField(
            model_name='security',
            name='position',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
