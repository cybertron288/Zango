"""
Module containing custom template filters
"""

from django import template
from django.conf import settings
import os
import re

register = template.Library()


@register.filter()
def humanize_timedelta(timedelta_obj):
    """
    Calculate the total number of days, hours, minutes, and seconds from the given timedelta object.
    Parameters:
    timedelta_obj (timedelta): A timedelta object representing a duration of time.
    Returns:
    str: A formatted string with the total days, hours, minutes, and seconds calculated from the timedelta object.
    """
    seconds = timedelta_obj.total_seconds()
    time_total = ""
    if seconds > 86400:  # 60sec * 60min * 24hrs
        days = seconds // 86400
        time_total += "{} days".format(int(days))
        seconds = seconds - days * 86400

    if seconds > 3600:
        hrs = seconds // 3600
        time_total += " {} hours".format(int(hrs))
        seconds = seconds - hrs * 3600

    if seconds > 60:
        mins = seconds // 60
        time_total += " {} minutess".format(int(mins))
        seconds = seconds - mins * 60

    if seconds > 0:
        time_total += " {} seconds".format(int(seconds))
    return time_total


@register.filter()
def update_latest(build_path):
    buildir = os.path.dirname(build_path)
    filep = os.path.basename(build_path)
    for dir in settings.STATICFILES_DIRS:
        for dirpath, dirnames, filenames in os.walk(dir):
            for filename in filenames:
                if re.match(filep, filename):
                    print(os.path.join(dirpath, filename))
                    return os.path.join(buildir, filename)
    return  build_path