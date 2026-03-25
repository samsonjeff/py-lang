import numpy as np
from numpy import array
# ways to import package


np.array([4,3,2,1])
array([1, 2, 3 ,4])


from numpy import array

fam = ["liz", 1.73, "emma", 1.68,
       "mom", 1.71, "dad", 1.89]

...
fam_ext = fam + ["me", 1.79]

...
print(str(len(fam_ext)) + " elements in fam_ext")

...
np_fam = array(fam)