# Generated by Django 3.0.9 on 2020-08-07 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0004_data_20200806_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pointofinterest',
            old_name='categories',
            new_name='dt_categories',
        ),
        migrations.RenameField(
            model_name='pointofinterest',
            old_name='datatourism_id',
            new_name='dt_id',
        ),
    ]
