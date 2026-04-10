import numpy as np

# example of a 2d array
# 2 rows and 5 columns
np_2d = np.array([[1,2,3,4,5],
                  [6,7,8,9,0]])

string_2d = np.array([[1,2,3,4,5],
                  ["6",7,8,9,0]]) #convert 1 and all will become string

a = string_2d[1][0]
b = type(a)
c = string_2d.dtype
d = string_2d.shape

print(f"print string data {a},type of data is {b}, data inside of string_2d {c}, shape of string_2d is {d} ")

#subsetting
print(string_2d[ : , 1:3])
#output     # [['2' '3']
            #  ['7' '8']]
print(string_2d[1, : ])