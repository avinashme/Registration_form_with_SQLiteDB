# Generated by Django 2.2.6 on 2019-10-22 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationdetails',
            name='mobile_number',
            field=models.CharField(max_length=10),
        ),
    ]