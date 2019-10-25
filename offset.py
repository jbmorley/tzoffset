#!/usr/bin/env python3

import argparse
import datetime
import pytz


def offset(timezone):
    tz = pytz.timezone(timezone)
    offset = tz.utcoffset(datetime.datetime.now()).total_seconds()
    return offset


def main():
    parser = argparse.ArgumentParser(description="Lightweight tool to give the UTC offset for a given timezone")
    parser.add_argument("timezone")
    options = parser.parse_args()
    print(offset(options.timezone))


if __name__ == "__main__":
	main()
