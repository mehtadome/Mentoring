import json 

import os
print("Working dir:", os.getcwd())

# if path fails, uncomment lines 3 & 4, and fix path to file
myfile = json.load(open("Problems/Fundamentals/Intro to Data Science/myjson.json"))
#print(myfile)


for i in myfile["Contacts"]:
    if "Ruchir" in i:
        print (i["Ruchir"])
    if "Hardeep" in i:
        print (i["Hardeep"])

