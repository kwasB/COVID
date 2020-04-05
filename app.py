import requests
import json
import urllib3
import urllib
import csv
import pandas as pd
import numpy as np


datasource = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/csv'
file = 'dataset.csv'

#Pull data from source and
urllib.request.urlretrieve(datasource, file)


df = pd.read_csv(file)

df2 = df.groupby(df['popData2018'])

data = df.set_index('geoId').to_dict()

mydict =

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