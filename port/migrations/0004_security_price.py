# Generated by Django 2.2.5 on 2019-09-08 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0003_security_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='security',
            name='price',
            field=models.CharField(max_length=200, null=True),
        ),
    ]