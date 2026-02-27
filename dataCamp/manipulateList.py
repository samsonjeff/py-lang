# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
print(areas)

# ways to replicate lists
#1
# areas_copy = list(areas)
#2
# areas_copy = areas[:]
#3
areas_copy = areas.copy()

print(areas_copy)
# Change areas_copy
areas_copy[0] = 5.0
del areas_copy[1]

print("show highest value" , max(areas_copy))
print("show lowest value" , min(areas_copy))

# Print areas
print(areas)
print(areas_copy)