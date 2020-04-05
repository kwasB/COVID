import requests
import json
import urllib3
import urllib
import csv
import pandas as pd
import numpy as np
from itertools import groupby
from collections import OrderedDict

datasource = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/csv'
file = 'dataset.csv'

#Pull data from source and
urllib.request.urlretrieve(datasource, file)

df = pd.read_csv(file, dtype={
    "dateRep": str, "day": str, "month": str, "year": str, "cases": str, "deaths": str,
    "countriesAndTerritories": str, "geoId": str, "countryterritoryCode": str, "popData2018": str
})
results = []
for geo, bag in df.groupby("geoId"):
    contents_df = bag.drop(["geoId"], axis=1)
    subset = [OrderedDict(row) for i, row in contents_df.iterrows()]
    results.append(OrderedDict([(geo, subset)]))
with open('ExpectedJsonFile.json', 'w') as outfile:
    outfile.write(json.dumps(results, indent=4))

dataset = [{
    'AF' : [{
        'geoId' : 'AF',
        'countriesAndTerritories' : 'Afghanistan',
        'countryterritoryCode': 'AFG',
        'cases' : 0,
        'deaths': 0,
        'date Rep' : '04/04/2020'
    },
    {
        'geoId': 'AF',
        'countriesAndTerritories': 'Afghanistan',
        'countryterritoryCode': 'AFG',
        'cases': 4,
        'deaths': 0,
        'date Rep': '03/04/2020'
    }]
}]