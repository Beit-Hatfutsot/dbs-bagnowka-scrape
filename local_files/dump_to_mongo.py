import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['bhdata']
photoUnits = db['photoUnits']

file = open("bagnowka_all.json", "r")
data = json.load(file)

#print(alll[slug])

count = 0
for slug in data:
    data[slug]["Header"]["He"] = "null"
    
    photoUnits.insert_one(data[slug])
    count += 1
    print("1 item was added to photoUnits")

print("{} items were inserted to photoUnits.".format(count))
