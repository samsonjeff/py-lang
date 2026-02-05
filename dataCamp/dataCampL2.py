# DATACAMP module 1 ( lists manipulation )

sampleData = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Subset the house list
sampleData[-1][1] = 9.8 # new value of chosen index
printOut = sampleData[-1][1]

newData = ["Garage", 30.5]

sampleData.append(["Garden", 20.5]) # other way to ADD data on list

sampleData.extend(newData) # other way to ADD data on list

del sampleData[-2:]

# print(printOut)
print(sampleData)