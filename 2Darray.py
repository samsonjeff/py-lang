import numpy as np

# example of a 2d array
# 2 rows and 5 columns
np_2d = np.array([[1,2,3,4,5],
                  [6,7,8,9,0]])

string_2d = np.array([[1,2,3,4,5],
                  ["6",7,8,9,0]]) #convert 1 and all will become string

print("type of" , type(string_2d))
print("data inside" , string_2d.dtype)
print("array shape" , string_2d.shape)