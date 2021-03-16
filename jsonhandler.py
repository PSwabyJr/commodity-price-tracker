"""jsonhandler.py
By: Lorenzo Swaby pswabyjr@gmail.com
Date Created: 3/15/2021
Description:
Script used to add data, read data and create new json file if it doesn't exist.
"""

import json
import os.path

def write_json(data, fileName):
  with open(fileName, 'w') as f:
    json.dump(data, f, indent =4)
    f.close()

def doesJsonFileExist(fileName):
  if !os.path.isfile(fileName):   # creates json file if it doesn't exist
     #create header for json file
     jsonHeaderName= {}
     jsonHeaderName[os.path.splitext(fileName)[0]]= []  #os.path.splitext()[0] removes .json extension from filename
     
     # create json file
     with open(fileName, 'w') as outfile:
      json.dump(jsonHeaderName, outfile, indent= 4)
     outfile.close()

# variable inputData is in dictionary format
def addDataToJsonFile(fileName, inputData):
  with open(fileName) as json_file:
    data= json.load(json_file)
    temp= data[os.path.splitext(fileName)[0]]
    temp.append(inputData)
  write_json(data, fileName)
  json_file.close()

# search for data and return dictionary (key,value) pairs if it exists within json file
def readDataFromJsonFile(fileName, key, value):
  with open(fileName) as json_file:
    data= json.load(json_file)
    library= data[os.path.splitext(fileName)[0]]
    #going through each key, value pair in dictionary
    for entry in library:
      if entry[key]== value:
        return entry  #return dictionary entry if (key, value) pair found
    return {}  # returns empty dictionary if (key,value) pair does not exist
  
  
