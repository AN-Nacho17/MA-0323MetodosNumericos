import numpy as np #Se importa numpy la cual es una libreria de python para realizar calculos numericos entre otras cosas
n = '' #Creacion de la variable n vacia para poder iniciar ciclo while posteriormente
while not n.isdigit(): # Verificacion de n hasta que sea un digito
    n = input("Ingrese el tamaño de la matriz (nxn): ")#Solicita el valor de n
    if not(n.isdigit()): # Verifica el valor de n, sino es un digito muestra un msj de error y vuelve a empezar el while
        print("Solo se permiten numeros enteros")
n=int(n)# una vez validado que n sea un digito se parsea
A = np.zeros((n,n)) #Crear matriz con 0 del tamano nxn para la matriz Original
U = np.zeros((n,n)) #Crear matriz con 0 del tamano nxn para la U
L = np.identity(n,dtype=float)#Crear L con la matriz identidad
P = np.identity(n)#Crear P con la matriz identidad
for r in range(0,n): #For que inicia en 0 hasta n para representar filas=rows
    for c in range(0,n): #For que inicia en 0 hasta n para representar columnas=columns
        A[(r),(c)]=float(input("Ingrese el elemento a[" +str(r+1)+str(c+1)+ "]: ")) #Se solicitan los datos de cada entrada de la matriz original
U = np.copy(A) #Copiar A en U para iniciar con el proceso
#Inicio del metodo
for i in range(0,n-1):
    columna = abs(U[i:,i]) #Obtener los valores en absoluto de la columna para buscar el pivote 
    nMayor = np.argmax(columna) #Se obtiene el indice del numero mayor
    if (nMayor !=0):
    # intercambio de filas en U y P  
        tempU = np.copy(U[i,:])
        tempP= np.copy(P[i,:])
        U[i,:] = U[nMayor+i,:]
        P[i,:] = P[nMayor+i,:]
        U[nMayor+i,:] = tempU
        P[nMayor+i,:] = tempP
        for z in range(i): #Intercambio de los valores en L cuando hay cambio de filas
            tempL= L[i,z]
            L[i,z]=L[nMayor+i,z]
            L[nMayor+i,z]=tempL
    pivote = U[i,i]
    siguiente = i+1
    for k in range(siguiente,n,1):
        factor = U[k,i]/pivote
        U[k,:] = U[k,:] - U[i,:]*factor
        L[k,i] = factor
# SALIDA
print("Matriz Original A=")
print(A)
print('Matriz U: ')
print(U)
print('matriz L: ')
print(L)
print('matriz P: ')
print(P)
print("PA")
print(np.dot(P,A))
print("LU")
print(np.dot(L,U))