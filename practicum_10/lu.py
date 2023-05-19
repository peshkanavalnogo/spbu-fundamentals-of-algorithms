import numpy as np
from numpy.typing import NDArray


def lu(A: NDArray, permute: bool) -> tuple[NDArray, NDArray, NDArray]:
    n = A.shape[0]
    L = np.eye(n)
    U = np.copy(A)
    P = np.eye(n)

    for k in range(n-1):
        if permute:
            max_index = np.argmax(np.abs(U[k:, k])) + k
            if max_index != k:
                U[[k, max_index]] = U[[max_index, k]]
                P[[k, max_index]] = P[[max_index, k]]
                if k > 0:
                    L[[k, max_index], :k] = L[[max_index, k], :k]
            if np.abs(U[k,k]) < 1e-20:
                raise ZeroDivisionError("Divide by zero during LU decomposition.")
        for j in range(k+1, n):
            if np.abs(U[j,k]) < 1e-20:
                raise ZeroDivisionError("Divide by zero during LU decomposition.")
            L[j, k] = U[j, k] / U[k, k]
            U[j, k:] -= L[j, k] * U[k, k:]

    return L, U, P


def solve(L: NDArray, U: NDArray, P: NDArray, b: NDArray) -> NDArray:
    n = L.shape[0]
    y = np.zeros(n)
    x = np.zeros(n)

    b = np.dot(P, b)

    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])
    for i in range(n-1 , -1 , -1):
        if np.abs(U[i,i]) < 1e-20:
            raise ZeroDivisionError("Divide by zero during back substitution.")
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]

    return x


def get_A_b(a_11: float, b_1: float) -> tuple[NDArray, NDArray]:
    A = np.array([[a_11, 1.0, -3.0], [6.0, 2.0, 5.0], [1.0, 4.0, -3.0]])
    b = np.array([b_1, 12.0, -39.0])
    return A, b


if __name__ == "__main__":
    # Let's implement the LU decomposition with and without pivoting
    # and check its stability depending on the matrix elements
    p = 9 # modify from 7 to 16 to check instability
    a_11 = 3 + 10**(-p)  # add/remove 10**(-p) to check instability
    b_1 = -16 + 10**(-p)   # add/remove 10**(-p) to check instability
    A, b = get_A_b(a_11, b_1)
    # With pivoting
    L, U, P = lu(A, permute=True)
    x = solve(L, U, P, b)
    assert np.all(np.isclose(x, [1, -7, 4])), f"The anwser {x} is not accurate enough"
    # Without pivoting
    L, U, P = lu(A, permute=False)
    x_ = solve(L, U, P, b)
    assert np.all(np.isclose(x_, [1, -7, 4])), f"The anwser {x_} is not accurate enough"
