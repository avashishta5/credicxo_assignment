# Generated by Django 3.1.2 on 2020-10-07 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='registration_no',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
