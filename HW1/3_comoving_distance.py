# This code uses Simpson’s rule to estimate comoving distance in a flat universe with Omega_m = 0.3, Omega_Lambda = 0.7 and H_0 = 67 km/s/Mpc
import numpy as np

# Constants
c = 3.0E5  # Speed of light in km/s
H0 = 67.0  # Hubble constant in km/s/Mpc
Omega_m = 0.3
Omega_Lambda = 0.7

# Function for E(z)
def E(z):
    return np.sqrt(Omega_m * (1 + z)**3 + Omega_Lambda)

# The integrand for comoving distance
def integrand(z):
    return 1 / E(z)

# Simpson's rule
def simpson_rule(a, b, N):
    '''
    Use simpson rule to integrate fuction f(x) between a and b
    '''
    if N % 2 == 1:
        raise ValueError("N must be even")
    h = (b - a) / N
    integral = integrand(a) + integrand(b)
    for i in range(1, N):
        if i % 2 == 0:
            integral += 2 * integrand(a + i * h)
        else:
            integral += 4 * integrand(a + i * h)
    return (h / 3) * integral

# Function to calculate the comoving distance
def comoving_distance(z, epsilon=1e-4):
    N = 2
    previous_estimate = 0
    count = 0
    while True:
        current_estimate = simpson_rule(0, z, N) # Calculate the comoving distance
        count += 1
        relative_error = abs(current_estimate - previous_estimate) / current_estimate # Get relative precision
        if relative_error < epsilon: # Check relative precision
            break
        previous_estimate = current_estimate
        N *= 2  # Double the number of intervals to refine the estimate
    return (c / H0) * current_estimate, count, relative_error

# Redshift values
redshifts = [1.0, 3.0, 8.2]

# Compute comoving distances for the given redshifts
for z in redshifts:
    D_c, count, relative_error = comoving_distance(z)
    print(f"Comoving distance for z = {z}: {D_c:.4f} Mpc with relative precision = {relative_error:g} in {count:d} steps")
    
