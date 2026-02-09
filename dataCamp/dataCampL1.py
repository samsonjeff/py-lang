# DATACAMP module 1 (lists & tuple) subsetting lists
import random

houseAreaName = ["hallway", 
"kitchen" ,
"livingRoom" ,
"bedRoom" ,
"bathRoom" ]

# generateArea = [[f"House area: {name}({round(random.uniform(1, 200), 2)} sqm)"] for name in houseAreaName]

generateArea = [[f"House_Area:{name} ({round(random.uniform(1, 200), 2)} sqm)"] for name in houseAreaName][::-1] # <-- reverse/slicing

# House information as list of lists

#print(houseArea[:2]) #retrieving list from index 0 to 1
# print(generateArea) #retrieving index tuple lists
# print(generateArea[0:4]) # 0 to index 4
# print(generateArea[:4]) # 0 to index 4
print(generateArea[4:]) # 4 to end