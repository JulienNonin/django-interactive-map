# Generated by Django 3.0.9 on 2020-08-12 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0013_data_populate_commune_20200812_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofinterest',
            name='city',
            field=models.CharField(max_length=50, verbose_name='commune', default='pas de commune'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='pointofinterest',
            name='city',
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='commune',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tourism.Commune'),
        ),
    ]
