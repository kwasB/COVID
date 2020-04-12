import json
import pandas as pd
import urllib


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
