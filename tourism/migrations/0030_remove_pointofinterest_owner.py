# Generated by Django 3.1.2 on 2020-10-04 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0029_place_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pointofinterest',
            name='owner',
        ),
    ]
