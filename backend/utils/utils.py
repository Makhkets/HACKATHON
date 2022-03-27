import string
from datetime import datetime, timedelta
from itertools import chain
from random import choice

import django_filters
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from transliterate import translit
from django.utils.translation import gettext_lazy as _

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 75
    page_size_query_param = 'page_size'
    max_page_size = 1000


def get_broken_label_ids(label_id_array):
    err_label_arr = []
    for label_id in label_id_array:
        events = Label.objects.filter(id=label_id)
        if len(events) == 0:
            err_label_arr.append(label_id)
    return err_label_arr


def validate_password(self, value: str) -> str:
    """
    Hash value passed by user.
    :param value: password of a user
    :return: a hashed version of the password
    """
    return make_password(value)


def get_token(length=15, only_digits=False):
    rand_str = lambda n: ''.join([choice(string.ascii_lowercase) for i in range(n)])
    if only_digits:
        rand_str = lambda n: ''.join([choice(string.digits) for i in range(n)])
    set_id = rand_str(length)
    return set_id

def get_closest_event(event_set):
    closest = event_set.filter(start_time__gte=datetime.now()).order_by("start_time").first()
    return closest


def get_closest_to_dt_from_two_eventsets(event_set_a, event_set_b, dt):
    event_a = event_set_a.filter(start_time__gte=dt).order_by("start_time").first()
    event_b = event_set_b.filter(start_time__gte=dt).order_by("start_time").first()

    if event_a and event_b:
        return event_a if abs(event_a.start_time - dt) < abs(event_b.start_time - dt) else event_b
    else:
        return event_a or event_b


def parse_int(s, base=10, val=None):
    try:
        a = int(s, base)
        return a
    except:
        return val


def parse_bool(s, val=False):
    try:
        if s.lower() in ['true', '1', 't', 'y', 'yes']:
            return True
        if s.lower() in ['false', '0', 'n', 'no']:
            return False
    except:
        return val


def get_events_by_date(date, user):
    # Get all events in date, linked to this user
    events_slaves = user.event_slaves.filter(Q(start_time__date=date))
    events_master = user.event_master.filter(Q(start_time__date=date))
    result_list = list(set(list(chain(events_slaves, events_master))))
    return result_list


def time_to_tz_naive(t, tz_in, tz_out):
    return tz_in.localize(datetime.combine(datetime.today(), t)).astimezone(tz_out).time()


def string_is_equal(string1, string2):
    import hashlib
    print("HASH")
    hash1 = int(hashlib.sha256(string1.encode('utf-8')).hexdigest(), 16) % 10 ** 8
    hash2 = int(hashlib.sha256(string2.encode('utf-8')).hexdigest(), 16) % 10 ** 8
    print(hash1)
    print(hash2)
    return hash1 == hash2


def my_translit(text):
    text = text.strip()
    try:
        text = translit(text, reversed=True)
    except:
        print('Translit false')
    text = "".join(e for e in text if e.isalnum())
    return text


def validate_positive(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )


def insert_keys_to_string(str, dict_of_values):
    t = string.Template(str)
    return t.safe_substitute(**dict_of_values)


def filter_array_by_unique_together(array, keys_array=[]):
    buffer_dict = {}
    for e in array:
        my_tuple = tuple([e[key] for key in keys_array])
        if my_tuple not in buffer_dict:
            buffer_dict[my_tuple] = e
    return buffer_dict.values()

def filter_queryset_by_unique_together(qs):
    buffer_dict = {}
    for e in qs:
        my_tuple = (e.key, e.value)
        if my_tuple not in buffer_dict:
            buffer_dict[my_tuple] = e
    return list(buffer_dict.values())

def yearsago(years, from_date=None):
    if from_date is None:
        from_date = datetime.now()
    try:
        return from_date.replace(year=from_date.year - years)
    except ValueError:
        # Must be 2/29!
        assert from_date.month == 2 and from_date.day == 29 # can be removed
        return from_date.replace(month=2, day=28,
                                 year=from_date.year-years)
        # If it's 2/29, and 18 years ago there was no 2/29, this function will return 2/28.
        # If you'd rather return 3/1, just change the last return statement to read:
        # return from_date.replace(month=3, day=1,
        #                          year=from_date.year - years)

def num_years(begin, end=None):
    if end is None:
        end = datetime.now()
    num_years = int((end - begin).days / 365.2425)
    if begin > yearsago(num_years, end):
        return num_years - 1
    else:
        return num_years

class CharInFilter(django_filters.rest_framework.BaseInFilter, django_filters.rest_framework.CharFilter):
    pass