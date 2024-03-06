import numpy as np
# a, b, c y d son las esquinas de la malla
b = int(input("Ingrese el valor de b: "))
d = int(input("Ingrese el valor de d: "))
# Los límites de i y j
N = int(input("Ingrese el valor de N: "))
M = int(input("Ingrese el valor de M: "))
v = float(input("Ingrese el valor de v (velocidad): "))

# Los pasos de i y j
h = b/N
k = d/M
p = (v*k)/h

# Inicializar la matriz
w = np.zeros((N+1, M+1))

# Defino las funciones (nos las da el profe al principio de cada ejercicio)
def f(x):
    # las x = a + h*i y las y = c + k*j
    if 1 <= x <= 3:
        return 1
    else:
        return 0

def g(x):
    return 0

# Condiciones de frontera
for i in range(1, N):
    w[i][0] = f(h*i)
    w[i][1] = w[i][0] + k*g(h*i)
    
for j in range(1, M):
    w[0][j] = 0
    w[N][j] = 0
    
#recorremos los puntos interiores de la malla
for j in range(1, M):
    for i in range(1, N):
        w[i][j+1] = 2*(1-p**2)*w[i][j] + (p**2)*(w[i+1][j] + w[i-1][j]) - w[i][j-1]

print(w[i][j])

# Mostrar la solución
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define las coordenadas x y y de la malla
x = np.linspace(0, b, N+1)
y = np.linspace(0, d, M+1)

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
            

# el laplaciano es la divergencia del gradiente. el gradiente es el triangulo para abajo. osea que la A = traángulo al cuadrado
#nos va a preguntar por un análisis de la gráfica
# el laplaciano minimiza la energia. es como cuando una lona en tensión cae por su propio peso, hace que la tension sea la minima 

'''
Ejercicio 1:
f(x) = x(b-x)
g(x) = 0
'''

'''
Ejercicio 2
f(x) = x en x < b/2
       b - x en x > b/2
'''
''' 
Ejercicio 3
f(x) = 0
g(x) = sen(x)
b = pi
'''

'''
Ejercicio 4
f(x) = 0 
       1 en 1 < x < 3
b = 6
d = 24
N = 600
M= 2400
v = 0.5
'''