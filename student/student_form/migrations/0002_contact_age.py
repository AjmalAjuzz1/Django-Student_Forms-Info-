# Generated by Django 4.1.3 on 2022-11-14 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
