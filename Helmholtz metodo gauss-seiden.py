# MÉTODO REGRESIVO 
# EDP ELIPTICA CUANDO TIENE LAS DOS DERIVADAS DOBLES

import numpy as np
# a, b, c y d son las esquinas de la malla
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
d = int(input("Ingrese el valor de d: "))
# Los límites de i y j
N = int(input("Ingrese el valor de N: "))
M = int(input("Ingrese el valor de M: "))

# Valor de lambda 
l = int(input("Ingrese el valor de lambda: "))

# Los pasos de i y j
h = (b-a)/N
k = (d-c)/M


# Inicializar la matriz
w = np.zeros((N+1, M+1))

# Defino la funcion
def funcion(i, j):
    # las x = a + h*i y las y = c + k*j
    return 0

# Condiciones de frontera
for i in range(1, N):
    w[i][0] = 0
    w[i][M] = 0
    
for j in range(1, M):
    w[0][j] = 0
    w[N][j] = 1
    
#recorremos los puntos interiores de la malla
for rana in range(100): 
    for i in range(1, N):
        for j in range(1, M):
            w[i][j] = (k**2 * (w[i+1][j] + w[i-1][j]) + h**2 * (w[i][j+1] + w[i][j-1]) - h**2 * k**2 * funcion(i, j)) / (2*(h**2 + k**2) - (h*k*l)**2)
print(w[i][j])
# Mostrar la solución
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define las coordenadas x y y de la malla
x = np.linspace(a, b, N+1)
y = np.linspace(c, d, M+1)

# Crea una malla 2D con numpy
X, Y = np.meshgrid(x, y)

# Grafica la función Z como una superficie en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, w.T, cmap='viridis')

# Etiqueta los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Muestra la gráfica
plt.show()
'''el codigo es igual pero sale un -h**2*k**2*l**2 en el denominador de la ecuacion de relajacion'''
''' 
ecuacion de Helmholtz
u_xx + u_yy + lambda*u = f(x,y)
donde f(x,y) = 0
u(0,y) = u(x,0) = u(x, 1) = 0
u(1, y) = 1
vamos a hacer 3 casos
1. lambda = 1
2. lambda = 300
3. lambda = 1000
'''