#!/usr/bin/env python3

import datetime
import pytz


def offset(timezone):
    tz = pytz.timezone(timezone)
    offset = tz.utcoffset(datetime.datetime.now()).total_seconds()
    return offset
