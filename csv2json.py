import csv
import json

csvfile = open('shipDetections.csv', 'r')
jsonfile = open('predictions.json', 'w')

fieldnames = ("ShipDetections","Latitude","Longitude","Detected_width","Detected_length")
reader = csv.DictReader( csvfile, fieldnames)
count=0
jsonfile.write("[")
for row in reader:
    if count>1:
        jsonfile.write(",\n")
        json.dump(row, jsonfile)
    elif count==1:
        json.dump(row,jsonfile)
    count=count+1
jsonfile.write("]")