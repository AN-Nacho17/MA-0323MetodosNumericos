import numpy as np
from tabulate import tabulate

def perform_PLU_decomposition(A):
    tamano = np.shape(A)
    n = tamano[0]
    L = np.identity(n, dtype=float)
    P = np.identity(n)
    U = np.copy(A)

    for i in range(0, n-1):
        columna = abs(U[i:, i])
        nMayor = np.argmax(columna)
        if nMayor != 0:
            tempU = np.copy(U[i, :])
            tempP = np.copy(P[i, :])
            U[i, :] = U[nMayor+i, :]
            P[i, :] = P[nMayor+i, :]
            U[nMayor+i, :] = tempU
            P[nMayor+i, :] = tempP
            for z in range(i):
                tempL = L[i, z]
                L[i, z] = L[nMayor+i, z]
                L[nMayor+i, z] = tempL
        pivote = U[i, i]
        siguiente = i+1
        for k in range(siguiente, n, 1):
            factor = U[k, i] / pivote
            U[k, :] = U[k, :] - U[i, :] * factor
            L[k, i] = factor

    print("Matriz Original A: ")
    print(tabulate(A, tablefmt="fancy_grid"))
    print('Matriz U: ')
    print(tabulate(U, tablefmt="fancy_grid"))
    print('matriz L: ')
    print(tabulate(L, tablefmt="fancy_grid"))
    print('matriz P: ')
    print(tabulate(P, tablefmt="fancy_grid"))
    print("PA")
    print(tabulate(np.dot(P, A), tablefmt="fancy_grid"))
    print("LU")
    print(tabulate(np.dot(L, U), tablefmt="fancy_grid"))

if __name__ == "__main__":
    A = np.array([[2,-1,4,1,-1], [-1,3,-2,-1,2],[5,1,3,-4,1],[3,-2,-2,-2,3],[-4,-1,-5,3,-4]], dtype=float)
    perform_PLU_decomposition(A)
