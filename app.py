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
    "countriesAndTerritories": str, "geoId": str, "countryterritoryCode": str, "popData2018": str})

dfobj = df.to_dict(orient='records')

results2 ={}

for i in dfobj:
    CC_id = i.get('countryterritoryCode')
    if CC_id not in results2:
        results2[CC_id] = [i]
        print('not in dict: ',CC_id,i )
    else: results2[CC_id].append(i)

resultsJson = json.dumps(results2)

"""

dfCouCode = df['countryterritoryCode'].copy()

couCodeList = dfCouCode.tolist()

#list of country
couCodeList

dfCouCode.drop_duplicates(keep='first',inplace=True)

for CCode in couCodeList:



testCode = 'AZE'



resultsJson = json.dumps(results)

resultsJson = json.loads(results)



# results = []
# for geo, bag in df.groupby("geoId"):
#     contents_df = bag.drop(["geoId"], axis=1)
#     subset = [OrderedDict(row) for i, row in contents_df.iterrows()]
#     results.append(OrderedDict([(geo, subset)]))
# with open('ExpectedJsonFile.json', 'w') as outfile:
#     outfile.write(json.dumps(results, indent=4))

# dataset1 = {
#     'AF' : [{
#         'geoId' : 'AF',
#         'countriesAndTerritories' : 'Afghanistan',
#         'countryterritoryCode': 'AFG',
#         'cases' : 0,
#         'deaths': 0,
#         'date Rep' : '04/04/2020'
#     },
#     {
#         'geoId': 'AF',
#         'countriesAndTerritories': 'Afghanistan',
#         'countryterritoryCode': 'AFG',
#         'cases': 4,
#         'deaths': 0,
#         'date Rep': '03/04/2020'
#     }],
# 'AH' : [{
#         'geoId' : 'AF',
#         'countriesAndTerritories' : 'Afghanistan',
#         'countryterritoryCode': 'AFG',
#         'cases' : 0,
#         'deaths': 0,
#         'date Rep' : '04/04/2020'
#     },
#     {
#         'geoId': 'AF',
#         'countriesAndTerritories': 'Afghanistan',
#         'countryterritoryCode': 'AFG',
#         'cases': 4,
#         'deaths': 0,
#         'date Rep': '03/04/2020'
#     }]
#
# }
#
#
#
# for i in dfobj:
#     CC_id = i.get('countryterritoryCode')
#     if CC_id == testCode:
#         if CC_id not in newResults.keys():
#             newResults[testCode] = i
#         else: newResults.update(i)

# for i in dfobj:
#     CC_id = i.get('countryterritoryCode')
#     if CC_id == testCode:
#         if CC_id not in newResults.keys():
#             newResults[testCode] = i
#         else: newResults.update(i)

"""