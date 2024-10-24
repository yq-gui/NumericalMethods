# This code is a direct matrix solver using Cholesky decomposition dealing with a well-known ill-conditioned matrix - Hilbert matrix. Numerical instability in solving equations with Hilbert matrix will also be discussed, which is due to condition number of Hilbert matrix.
import numpy as np

def generate_hilbert_matrix(n, dtype):
    """
    Generate Hilbert matrix.
    """
    A = np.ones((n, n), dtype = dtype)
    for i in range(n):
        A[i] = 1/np.arange(i + 1, i + n + 1, 1)
    return A

def cholesky_decomposition(A, dtype, epsilon=1e-15):
    """
    Perform Cholesky decomposition on a symmetric positive-definite matrix A.
    Returns the lower triangular matrix L such that A = L * L^T.
    """
    n = A.shape[0]
    A_reg = A + np.eye(n) * epsilon # Avoid round-off error when n is large
    L = np.zeros_like(A, dtype = dtype)
    for i in range(n):
        for j in range(i + 1):
            sum_k = sum(L[i,:j] * L[j,:j]) 
            if i == j:
                L[i][j] = np.sqrt(A_reg[i][i] - sum_k)  # L_ij for i == j
            else:
                L[i][j] = (A_reg[i][j] - sum_k) / L[j][j] # L_ij for i != j
    return L

def cholesky_solver(A, b, dtype):
    """
    Solve Ax = b using Cholesky decomposition.
    """
    L = cholesky_decomposition(A, dtype = dtype)

    # Solve Ly = b using forward substitution
    y = np.zeros_like(b, dtype = dtype)
    for i in range(len(b)):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    # Solve L^T x = y using backward substitution
    x = np.zeros_like(b, dtype = dtype)
    for i in range(len(b) - 1, -1, -1):
        x[i] = (y[i] - np.dot(L.T[i, i + 1:], x[i + 1:])) / L[i, i]

    return x

###################################################### 
## solve Ax=b for n = 5 (single precision)
n = 5 
dtype = np.float32
print("------Single Precision------")
A = generate_hilbert_matrix(n, dtype = dtype)
L = cholesky_decomposition(A, dtype = dtype)
print("Decomposed matrix L:\n", L)

b = np.ones(n, dtype = dtype)
for i in range(len(b)):
    b[i] = sum(1/(1 + i + j) for j in range(n))

x = cholesky_solver(A, b, dtype = dtype)
print("Solution x:", x)
relative_error = max(x-np.ones(n, dtype = dtype))
print("Relative error:", relative_error)

## solve Ax=b for n = 5 (double precision)
n = 5 
dtype = np.float64
print("------Double Precision------")
A = generate_hilbert_matrix(n, dtype = dtype)
L = cholesky_decomposition(A, dtype = dtype)
print("Decomposed matrix L:\n", L)

b = np.ones(n, dtype = dtype)
for i in range(len(b)):
    b[i] = sum(1/(1 + i + j) for j in range(n))

x = cholesky_solver(A, b, dtype = dtype)
print("Solution x:", x)
relative_error = max(x-np.ones(n, dtype = dtype))
print("Relative error:", relative_error)
###################################################### 

###################################################### 
## At what n, relative error will larger than 50%? (single precision)
n = 5
dtype = np.float32
while True:
    A = generate_hilbert_matrix(n, dtype = dtype)
    b = np.ones(n, dtype = dtype)
    for i in range(len(b)):
        b[i] = sum(1/(1 + i + j) for j in range(n))
    x = cholesky_solver(A, b, dtype = dtype)
    relative_error = max(abs(x-np.ones(n, dtype = dtype)))
    if relative_error >= 0.5:
        break
    n += 1
print(f"For SINGLE precision, when n = {n}, relative error will larger than 50% and the solution becomes unstable.")

## At what n, relative error will larger than 50%? (double precision)
n = 5
dtype = np.float64
while True:
    A = generate_hilbert_matrix(n, dtype = dtype)
    b = np.ones(n, dtype = dtype)
    for i in range(len(b)):
        b[i] = sum(1/(1 + i + j) for j in range(n))
    x = cholesky_solver(A, b, dtype = dtype)
    relative_error = max(abs(x-np.ones(n, dtype = dtype)))
    if relative_error >= 0.5:
        break
    n += 1
print(f"For DOUBLE precision, when n = {n}, relative error will larger than 50% and the solution becomes unstable.")
###################################################### 

###################################################### 
def calculate_condition_number(A):
    """
    Calculate the condition number of a matrix A based on infinity-norm.
    """
    n = A.shape[0]
    C = np.ones(n, dtype = np.float64)
    for i in range(n):
        C[i] = sum(abs(A[i])) # infinity-norm
    return max(C)

n_list = [3, 6, 9, 12]
for n in n_list:
    condition_number = calculate_condition_number(generate_hilbert_matrix(n, dtype = np.float64))
    print(f"Condition number for n = {n}: ",condition_number)

# As can be seen, as n becomes larger, the condition number of A is larger, which means A is more ill-conditioned.
###################################################### 

# Suggestion:Use Sigular Value Decomposition.
# Sigular value decomposition can handle ill-conditioned matrix by isolating and controlling the components that contribute to numerical instability.