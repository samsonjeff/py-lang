#method a functions that belongs to the object
#ex. int str float lists etc.

import numpy as np

fam = ['liz', 1.73, 'loz', 1.83, 'laz', 1.93, 'lez', 1.13,]

# roundList = np.round(fam, 1)

indexOf = fam.index('laz') #Call method index() of chosen list

countOf = fam.index('liz') #index position

girl = fam[0]
# The "l0ong way"
name_list = list(girl.replace('z', 's')) # ['l', 'i', 's']
name_list.reverse()                      # Reverses the list in-place
rep = "-".join(name_list)


fam.append('new_user')

print(rep, indexOf, countOf, fam, type(fam))


###------------------- activity ---------------------- ###
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()
# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))
