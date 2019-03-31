# This script extracts the important classes from the metadata and stores it inside a csv file

import csv
import json
import pandas as pd

# Initializiing all the neccessary variables
data = ""
dataCSV = []
filePath = "C:/Users/narcg/Documents/ISIC-Archive-Downloader/Data/Descriptions/ISIC_"
dct = {"ID": "ImageName", "benignMalignant": "bOrM"}

# Loop through the directory 10,000 times
for i in range(10000):
    # Add image number to the path to get the right metadata
    filePath += str(i).zfill(7)
    
    # Read the json file and parse the data into a dictionary
    f = open(filePath, "r")
    for line in f.readlines():
        data += line
    data = json.loads(data)

    # Extract the useful info from the dictionary
    dct['ID'] = data['name']
    dct['benignMalignant'] = data['meta']['clinical']['benign_malignant']

    # Append the useful dictionary to the list for csv file
    dataCSV.append(dct)
    dct = dct.copy()

    # Erase all metadata to make room for new file
    data = ""
    f.close()
    filePath = "C:/Users/narcg/Documents/ISIC-Archive-Downloader/Data/Descriptions/ISIC_"
     
#print(dataCSV)
pd.DataFrame(dataCSV).sort_index().to_csv('classification.csv', index=False)

