# Generated by Django 3.1.2 on 2020-10-06 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('year', models.CharField(choices=[('I', 'First'), ('II', 'Second'), ('III', 'Third'), ('IV', 'Fourth')], max_length=3)),
                ('branch', models.CharField(choices=[('IT', 'Information Technology'), ('CSE', 'Computer Science'), ('ETC', 'Electronics & Telecommunications'), ('EE', 'Electrical Engineering'), ('ME', 'Mechanical Engineering')], max_length=3)),
                ('guardian_name', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('branch', models.CharField(choices=[('IT', 'Information Technology'), ('CSE', 'Computer Science'), ('ETC', 'Electronics & Telecommunications'), ('EE', 'Electrical Engineering'), ('ME', 'Mechanical Engineering')], max_length=3)),
                ('phone_no', models.CharField(max_length=10)),
            ],
        ),
    ]
