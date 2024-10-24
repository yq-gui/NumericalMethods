# This code is used to determine the smallest positive number in each data type. 
# Note that smallest positive number isn't always normalized number, so it could be different with the number in course slides.
import numpy as np

def smallest_positive_number(data_type):
    if data_type == 'int32':
        dtype = np.int32
    elif data_type == 'int64':
        dtype = np.int64
    elif data_type == 'float32':
        dtype = np.float32
    elif data_type == 'float64':
        dtype = np.float64
    else:
        raise ValueError("data type must be 'int32', 'int64', 'float32' or 'float64'.")
    # define initial positive number
    min_positive = dtype(1.0)
    # use recrusive algorithm to find minimum positive number
    while dtype(min_positive/2.0) > dtype(0):
            min_positive /= dtype(2.0)
    return min_positive

# smallest positive number for short int
f_min_int32 = smallest_positive_number('int32')
print("smallest positive number for short int is: ", f_min_int32)

# smallest positive number for long int
f_min_int64 = smallest_positive_number('int64')
print("smallest positive number for long int is: ", f_min_int64)

# smallest positive number for single float
f_min_float32 = smallest_positive_number('float32')
print("smallest positive number for single float is: ", f_min_float32)

# smallest positive number for double float
f_min_float64 = smallest_positive_number('float64')
print("smallest positive number for double float is: ", f_min_float64)