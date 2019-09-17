# Generated by Django 2.2.5 on 2019-09-12 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0006_auto_20190909_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='business',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='description',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='port.Security'),
        ),
    ]