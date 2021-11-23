#Destination Recommender System

###Mounting Drive and Importing Libraries

from google.colab import drive
drive.mount('/content/gdrive')

import pandas as pd 
import numpy as np
from datetime import datetime

###Before processing initial data

# #create the newDF set for all the data and then create its twoDArray
# newDF = set()
# thisset = set(df["'DESTINATION'"].value_counts().index)
# newDF.update(thisset)
# thisset = set(df["'ORIGIN'"].value_counts().index)
# newDF.update(thisset)
# newDF = list(newDF)

#textfile = open("/content/gdrive/MyDrive/TravelVerse/newDF.txt", "w")
#for element in newDF:
 # textfile.write(element + "\n")
#textfile.close()

#length = len(newDF)
#twoDArray = np.zeros((length, length, 13), np.int64)

###If reconnecting after processing initial data

# newDF = []
# with open('/content/gdrive/MyDrive/TravelVerse/newDF.txt') as f:
#   lines = f.readlines()
# for ele in lines:
#   newDF.append(ele.split("\n")[0])

# loadedArr = pd.read_csv("/content/gdrive/MyDrive/TravelVerse/chhehKalol.csv", header = None, delimiter=",")
# loadedArr = loadedArr.to_numpy()
# twoDArray = loadedArr.reshape(loadedArr.shape[0], loadedArr.shape[1] // 13, 13)

###Loading dataset in chunks

data = "/content/gdrive/MyDrive/TravelVerse/travelverse-compressed-dataset.csv"

df = pd.read_csv(data, skiprows = [i for i in range(1, 50000000)], nrows = 10000000)

###Processing data

# Removing one way trips to remove noise from the data
df.drop(df.index[df["'TRIP_TYPE'"] == "'OW'"], inplace=True)

# Removing columns which are useless for the recommender system
df = df[["'SEG_NUMBER'", "'MARKETING_AIRLINE_CD'", "'ORIGIN'", "'DESTINATION'", "'DEPARTURE_DATE'"]]

# Removing trips with discontinuous Segment Number to clean the data
deleteRows = []
previousSegment = 0
for row in df.index:
  temp = df["'SEG_NUMBER'"][row]
  if temp == previousSegment + 1 or temp == 1:
    previousSegment = temp
  else:
    deleteRows.append(row)
    previousSegment = 0
df.drop(deleteRows, inplace = True)

# Removing journeys with different origins and previous destinations for consecutive segment numbers
previousSegment = 1000
destination = ""
isNotValid = False
deleteRows = []
for row in df.index:
  if previousSegment < df["'SEG_NUMBER'"][row]:
    if isNotValid == True:
      deleteRows.append(row)
    else:
      if df["'ORIGIN'"][row] != destination:
        previousSegment = df["'SEG_NUMBER'"][row]
        deleteRows.append(row)
        isNotValid = True
      else:
        destination = df["'DESTINATION'"][row]
        previousSegment = df["'SEG_NUMBER'"][row]
  else:
    destination = df["'DESTINATION'"][row]
    previousSegment = df["'SEG_NUMBER'"][row]
    isNotValid = False
df.drop(deleteRows, inplace = True)

# Removing two trips mixing up together due to incomplete segment numbers
finalOrigin = ""
isNotValid = False
deleteRows = []
destination = ""
previousSegment = 1000
for row in df.index:
  if previousSegment < df["'SEG_NUMBER'"][row]:
    if isNotValid == True:
      deleteRows.append(row)
    else:
      destination = df["'DESTINATION'"][row]
      previousSegment = df["'SEG_NUMBER'"][row]
      if finalOrigin == destination:
        isNotValid = True
  else:
    finalOrigin = df["'ORIGIN'"][row]
    previousSegment = df["'SEG_NUMBER'"][row]
    isNotValid = False
df.drop(deleteRows, inplace = True)

# Removing trips with different initial origin and final destination
origin = ""
destination = ""
previousSegment = 1000
deleteRows = []
indexes = df.index
count = 0
for row in df.index:
  if previousSegment < df["'SEG_NUMBER'"][row]:
    destination = df["'DESTINATION'"][row]
  else:
    if previousSegment != 1000:
      if origin != destination:
        n = count
        temp = previousSegment
        while temp != 0:
          deleteRows.append(indexes[n - temp])
          temp = temp - 1
    origin = df["'ORIGIN'"][row]
  count += 1
  previousSegment = df["'SEG_NUMBER'"][row]
df.drop(deleteRows, inplace = True)

# Handling the non flight segment
indexes = df.index
count = 0
for row in df.index:
  if df["'MARKETING_AIRLINE_CD'"][row] == "'V'":
    if df["'SEG_NUMBER'"][row] == 1:
      df["'DEPARTURE_DATE'"][row] = df["'DEPARTURE_DATE'"][indexes[count + 1]]
    else:
      df["'DEPARTURE_DATE'"][row] = df["'DEPARTURE_DATE'"][indexes[count - 1]]
  count += 1

# Removing data without departure date
df = df[df["'DEPARTURE_DATE'"] != "'\\N'"]

# At this point the data only has trips which are useful for determining the number
# of people who travelled from a specific origin to a specific destination for vacation
# Creating the correlation matrix for recommendation from the data also defining the 
# destination of the trip as the airport where user spent 2 or more days

previousSegment = 1000
previousDate = ""
date_format = "'%Y-%m-%d'"
origin = 0
destination = 0
for row in df.index:
  if previousSegment < df["'SEG_NUMBER'"][row]:
    a = datetime.strptime(previousDate, date_format)
    b = datetime.strptime(df["'DEPARTURE_DATE'"][row], date_format)
    delta = b - a
    if delta.days > 1:
      destination = newDF.index(df["'ORIGIN'"][row])
      twoDArray[origin][destination][a.month] += 1
  else:
    origin = newDF.index(df["'ORIGIN'"][row])
  previousDate = df["'DEPARTURE_DATE'"][row]
  previousSegment = df["'SEG_NUMBER'"][row]

###Saving updated correlation matrix when processing in chunks

arrReshaped = twoDArray.reshape(twoDArray.shape[0], -1)
np.savetxt("/content/gdrive/MyDrive/TravelVerse/chhehKalol.csv", arrReshaped, delimiter=',')

###Giving Recommendations

# Give origin location in brackets
l1 = twoDArray[newDF.index("'BOM'")]

dictionary = {}
for i in range(len(l1)):
  dictionary[newDF[i]] = l1[i]
print(dictionary)

# Pass the month number as the 2nd argument in x
nayaVariable = sorted(dictionary.items(), key=lambda x: x[1][5], reverse = True)
print(nayaVariable)