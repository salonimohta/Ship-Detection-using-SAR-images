import csv
import json
import sys


def convert(loc):
    csvfile = open('./static/'+loc+'shipDetections.csv', 'r')
    jsonfile = open('./static/'+loc+'predictions.json', 'w')

    fieldnames = ("ShipDetections", "Latitude", "Longitude",
                  "Detected_length")
    reader = csv.DictReader(csvfile, fieldnames)
    count = 0
    jsonfile.write("[")
    for row in reader:
        if count > 1:
            jsonfile.write(",\n")
            json.dump(row, jsonfile)
        elif count == 1:
            json.dump(row, jsonfile)
        count = count+1
    jsonfile.write("]")


if __name__ == '__main__':
    loc = sys.argv[1]
    convert(loc)