#!/usr/bin/env python
# coding: utf-8
"""
This script demonstrates how to transform data from an API. It should be run AFTER data has been extracted (via the
extract.py script): this script should operate only on the files that exist locally on this machine -- it does NOT
make external HTTP requests.

The transform process vets and prepares a record for insertion in a database, but it does not do the insertion
(leave that to the loader).
"""

import json
import os
from datetime import datetime
from pyproj import Proj, transform
import load

STORAGE_DIRECTORY = "downloads"


def is_valid(record):
    """
    Is this a record we want to store?
    :param record: dictionary
    :return: boolean
    """
    if record['latitude'] == "99999" or record['longitude'] == "99999":
        return False

    return True


def convert_lat_lng(raw_lat, raw_lng):
    """
    Latitude and longitude in the dataset are given in accordance with [ESRI:102645 NAD 1983 StatePlane California V
    FIPS 0405 Feet](https://epsg.io/102645) format.
    In order to use those coordinates for our map visualization, we would need to transform geospatial coordinates from
    one coordinate reference system to another.
    Python offers the [PROJ](https://proj.org/index.html) library for performing conversions between
    cartographic projections.
    See http://pyproj4.github.io/pyproj/stable/api/transformer.html?highlight=transform#pyproj.transformer.transform

    This function is structured to work on single pair of coordinates.

    :param raw_lat: string
    :param raw_lng: string
    :return: tuple
    """
    pm = '+proj=lcc +lat_1=34.03333333333333 +lat_2=35.46666666666667 +lat_0=33.5 +lon_0=-118 +x_0=2000000 '\
         + '+y_0=500000.0000000002 +ellps=GRS80 +datum=NAD83 +to_meter=0.3048006096012192 +no_defs'

    latitude = float(raw_lat)
    longitude = float(raw_lng)
    lat_series, lng_series = transform(Proj(pm, preserve_units=True), Proj("+init=epsg:4326"), [latitude], [longitude])
    return lat_series[0], lng_series[0]


def transform_record(record):
    """
    Manipulate the record here.
    la_parking_citations_df.drop(['Marked Time','RP State Plate','Plate Expiry Date','VIN'], axis = 1, inplace = True)

    Sample input:
    {
      "ticket_number": "4273069625",
      "issue_date": "2015-12-30T00:00:00.000",
      "issue_time": "1030",
      "rp_state_plate": "CA",
      "plate_expiry_date": "201511",
      "make": "TOYT",
      "body_style": "PA",
      "color": "GY",
      "location": "107 HOBART BLVD",
      "route": "00479",
      "agency": "54",
      "violation_code": "80.69BS",
      "violation_description": "NO PARK/STREET CLEAN",
      "fine_amount": "73",
      "latitude": "99999",
      "longitude": "99999"
    }

    :param record: dictionary
    :return: dictionary
    """

    latitude, longitude = convert_lat_lng(record['latitude'], record['longitude'])

    return {
        "ticket_number": int(record['ticket_number']),
        "issue_date": datetime.strptime(record['issue_date'], '%Y-%m-%dT%H:%M:%S.%f'),
        "make": record['make'],
        "body_style": record['body_style'],
        "color": record['color'],
        "location": record['location'],
        "route": record['route'],
        "agency": record['agency'],
        "violation_code": record['violation_code'],
        "violation_description": record['violation_description'],
        "fine_amount": float(record['fine_amount']),
        "latitude": latitude,
        "longitude": longitude,
    }


def loop_over_records(records):
    for r in records:
        if is_valid(r):
            transformed = transform_record(r)
            load.save_violation(transformed)
            print(f"Saved {r['ticket_number']}")


def do_transform():
    for filename in os.listdir(STORAGE_DIRECTORY):
        if filename.endswith(".json"):
            with open(os.path.join(STORAGE_DIRECTORY, filename)) as file_object:
                loop_over_records(json.load(file_object))


if __name__ == "__main__":
    do_transform()

