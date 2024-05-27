import pandas as pd

def bisection(funcion, a, b, tol):

    #Función que obtiene la imagen a partir de una función definida.
    def f(x):
        return eval(funcion)

    #Cálculo inicial del error.
    error = abs(b - a)

    #Vector para almacenar los valores de a, b, c y el error luego de cada iteración.
    data = []

    #El criterio del ciclo consiste en que la ejecución seguirá hasta
    # que se sobrepase la tolerancia definida.
    while error > tol:

        #Cálculo del punto medio
        c = (b + a) / 2

        if f(a) * f(b) >= 0:
            return None  # No se encontró una raíz -
        #caso de error, la función se detiene.

        if f(c) == 0:
            return (0, c, c)  # Raíz exacta encontrada

        if f(c) * f(a) < 0:
            #El punto medio se convierte en el extremo
            # derecho del intervalo en desarollo.
            b = c
        else:
            #El punto medio se convierte en el extremo
            # izquierdo del intervalo en desarollo.
            a = c

        #Para todas las operaciones se cálcula el error
        # de manera que el ciclo pueda cerrarse
        # en algún momento de la ejecución.
        error = abs(b - a)

        #Se agregan los elementos a (extremo izquierdo), b (extremo derecho), c (punto medio) y el error al vector que los almacena.
        row = {'A': a, 'B': b, 'f(Pn)': c, 'Error': error}
        data.append(row)

    return pd.DataFrame(data)

if __name__ == "__main__":
    #Ejemplo de uso de la función bisection
    function = "x**3 + 2*x**2 + 10*x - 20" #función a evaluar
    a = -10 #extremo izquierdo del intervalo
    b = 10 #extremo derecho del intervalo
    tol = 1e-9 #tolerancia
    result = bisection(function, a, b, tol) #Llamado a la función

    result.insert(0, 'Número de iteración', result.index) #Se agrega una columna con el número de iteración

    #Configuración necesaria para mostrar los resultados con 9 decimales.
    pd.set_option('display.float_format', '{:.9f}'.format)

    print(result)