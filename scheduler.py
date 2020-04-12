import schedule
import time
import urllib

datasource = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/csv'
file = 'dataset.csv'

def job(file,datasource):
    urllib.request.urlretrieve(datasource, file)

schedule.every().day.at('19:54').do(job,file,datasource)

while True:
    schedule.run_pending()
    time.sleep(1)
