# Generated by Django 3.0.9 on 2020-08-06 16:27


from django.db import migrations
import json
from os.path import dirname, join
import os
from django.contrib.gis.geos import fromstr


def modify_from_data_tourism(apps, schema_editor):
    PointOfInterest = apps.get_model('tourism', 'PointOfInterest')
    Category = apps.get_model('tourism', 'Category')

    ### create categories
    event = Category(name="Évènements", tag="event", icon="koamaru", order=2)
    tourism_info = Category(name="Accueil touristique", tag="tourism-info", icon="blue", order=4)
    natural_site = Category(name="Sites naturels remarquables", tag="natural-site", icon="natural-site", order=6)
    city = Category(name="Villages", tag="city", icon="orange", order=8)
    cultural_site = Category(name="Sites architecturaux remarquables", tag="cultural-site", icon="default", order=10)
    accommodation = Category(name="Hébergements", tag="accommodation", icon="glamour", order=12)
    food = Category(name="Restauration", tag="food-establishment", icon="purple", order=14)
    tour = Category(name="Parcours de randonnées", tag="tour", icon="brown", order=16)
    
    natural_site.save()
    cultural_site.save()
    city.save()
    tour.save()
    tourism_info.save()
    food.save()
    accommodation.save()
    event.save()

    ### 
    flux_dir = "flux-7559-202008071000"
    root_dir = join(dirname(dirname(__file__)), 'data/tourism', flux_dir, 'objects')

    i = 0
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            i += 1
            with open(join(subdir, file)) as f:
                obj = json.load(f)
            if 'PointOfInterest' in obj['@type']:
                # Find the corresponding POI
                try:
                    poi = PointOfInterest.objects.get(dt_id = obj["@id"])
                    categories = obj['@type']
                except (KeyError, TypeError, IndexError):
                    continue

                if "EntertainmentAndEvent" in categories:
                    poi.category = event
                elif "Accommodation" in categories:
                    poi.category = accommodation
                elif "FoodEstablishment" in categories:
                    poi.category = food
                elif "Tour" in categories:
                    poi.category = tour
                elif "CulturalSite" in categories:
                    poi.category = cultural_site
                elif "NaturalHeritage" in categories:
                    poi.category = natural_site
                elif "PlaceOfInterest" in categories:
                    poi.category = tourism_info

                print(i, '\t', poi.name)

                poi.save()

def delete_data_tourism(apps, schema_editor):
    PointOfInterest = apps.get_model('tourism', 'PointOfInterest')
    Category = apps.get_model('tourism', 'Category')
    default_cat = Category.objects.get(tag="default")
    db_alias = schema_editor.connection.alias
    for poi in PointOfInterest.objects.using(db_alias).exclude(dt_id=""):
        poi.category = default_cat
        poi.save()
    
    for cat in Category.objects.exclude(tag="default"):
        cat.delete()
    
class Migration(migrations.Migration):
    dependencies = [
        ('tourism', '0006_auto_20200807_1533'),
    ]

    operations = [
        migrations.RunPython(modify_from_data_tourism, delete_data_tourism)
    ]
