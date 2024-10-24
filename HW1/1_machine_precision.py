# This code is used to determine the machine precision for single and double float.
import numpy as np

def machine_precision(precision):
    if precision == 'single':
        dtype = np.float32
    elif precision == 'double':
        dtype = np.float64
    else:
        raise ValueError("precision must be 'single' or 'double'")
    # define initial precision
    epsilon = dtype(1.0)
    # find the epsilon_m that can make 1 + epsilon_m and 1 different
    while dtype(1.0) + epsilon != dtype(1.0):
        epsilon /= dtype(2.0)
    return epsilon * dtype(2.0)

# machine precision for single float
single_precision_epsilon = machine_precision('single')
print("machine precision for single float is: ", single_precision_epsilon)

# machine precision for double float
double_precision_epsilon = machine_precision('double')
print("machine precision for double float is: ", double_precision_epsilon)