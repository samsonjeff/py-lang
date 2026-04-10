import numpy as np

# example of a 2d array
# 2 rows and 5 columns
np_2d = np.array([[1,2,3,4,5],
                  [6,7,8,9,0]])

string_2d = np.array([[2,1,3,5,4],
                  ["6",8,0,9,7]]) #convert 1 and all will become string

a = string_2d[1][0]
b = type(a)
c = string_2d.dtype
d = string_2d.shape
e = string_2d.ndim
f = np.median(string_2d.astype(float)) #find median and convert it into float
g = np.sort(string_2d[:,:].astype(int)) # sort each row


print(f"print string data {a},type of data is {b}, data inside of string_2d {c}, shape of string_2d is {d} ")

#subsetting
print(string_2d[ : , 1:3])
#>          # [['2' '3']
            #  ['7' '8']]

print(string_2d[1, : ])
#> ['6' '7' '8' '9' '0']

# check the count of dimention to determine
print(e)

print(f"display median {f}")

print(f"display sort {g}")