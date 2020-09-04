import datetime
from .models import Category, Commune, OpeningHoursSchema, OpeningHours, PointOfInterest

def get_isoweekdays_btw_dates(d1, d2):
    if (d2 - d1).days >= 7:
        return list(range(1, 8))
    wd1, wd2 = d1.isoweekday(), d2.isoweekday()
    if wd1 <= wd2 :
        return list(range(wd1, wd2+1))
    else:
        return [j % 7 + 1 for j in range(wd1 - 1, wd2 + 7)]


def get_opening_schema_for_period(poi, date_start, date_end):
    return poi.openinghoursschema_set.filter(
        valid_from__lte = date_end,
        valid_through__gte = date_start,
        openinghours__weekday__in = get_isoweekdays_btw_dates(date_start, date_end)
    ).distinct()

def is_open(poi, date_start, date_end):
    return get_opening_schema_for_period(poi, date_start, date_end).count() != 0