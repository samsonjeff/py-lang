# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
print(areas)

#min max functionsls
highest = max(areas)
lowest = min(areas)

print("show highest value" , highest)
print("show lowest value" , lowest)

#round to 2
rounding = [round(area , ndigits=None) for area in areas]

print("rounding", rounding)