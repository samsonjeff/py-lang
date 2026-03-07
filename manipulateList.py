# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
print("lists origin", areas)

# ways to replicate lists
#1
# areas_copy = list(areas)
#2
# areas_copy = areas[:]
#3
areas_copy = areas.copy()
print("copy origin" , areas_copy)

# Change areas_copy
areas_copy[0] = 5.0
del areas_copy[1]

# Print areas
print(areas)
print(areas_copy)