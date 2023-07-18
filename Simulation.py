import csv
import time
import pyrebase
from collections.abc import Mapping, MutableMapping
from FirebaseConfig import firebase
dataFeedRate = 10
dataSource = 'Waterlevel.csv'
storage = firebase.storage()
database = firebase.database()

# Open the CSV file
with open(dataSource, 'r') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)
    
    # Skip the header row
    next(csvreader)
    i = 2
    # Loop through the data and simulate a timeline
    while i < 15:
        for row in csvreader:
            coord = row[1]
            Loc = row[0]
            water_lvl = row[i]
            # Print the timestamp and data
            print(f'Loc: {coord} | Waterlevel: {water_lvl}')
            data = {
                "Location" : coord,
                "Place" : Loc,
                "Distance" : water_lvl
            }
            database.set(data)
            
            # Wait for x seconds before continuing
            time.sleep(dataFeedRate)
        i += 1
        csvfile.seek(0)
        next(csvreader)
        
        # Wait for y seconds before continuing to the next row
        time.sleep(2)
    