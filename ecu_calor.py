# ESTE ES DIFERENCIA PROGRESIVA PORQUE USAMOS LOS VALORES ANTERIORES
# EDP PARABÓLICAS SI HAY UNA DE LAS DERIVADAS DOBLES
import numpy as np

# a, b, c y d son las esquinas de la malla
b = int(input("Ingrese el valor de b: "))
d = int(input("Ingrese el valor de d: "))
# Los límites de i y j
N = int(input("Ingrese el valor de N: "))
M = int(input("Ingrese el valor de M: "))
v = float(input("Ingrese el valor de v (conductividad): "))

# Los pasos de i y j
h = b/N
k = d/M

w = np.zeros((N+1, M+1))

def f(x):
    if 0 < x < b/2:
        return 1
    elif b/2 < x < b:
        return 0
    else:
        return 0

# Condiciones de frontera
for i in range(1, N):
    w[i][0] = f(i*h)
    w[i][1] = 0
    
for j in range(1, M):
    w[0][j] = 0
    w[N][j] = 0
    
for j in range(0, M):
    for i in range(1, N):
        w[i][j+1] = (1-2*k*v**2/h**2)*w[i][j] + (k*v**2/h**2)*(w[i+1][j] + w[i-1][j])
        
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
            
'''
Ejercicio 1
f(x) = e^(-(x-b/2)^2)
b= 5
d = 10
N= 40
M = 400
0.2 <v < 1.5

cuando el parámetro de la conductividad aumenta quiere decir que conduce peor,
entonces hay un pico y se disipa más rápido

Hay un limite en el parametro de h/raiz(2k). En este caso es 0.55

Las curvas características hacen que el calor se halle en un pico y se disperse. Como hay una característica, 
que habría que calcularla. En las ecuaciones de ondas había 2.
El calor fluye por la característica y se disipa por los laterales
'''

'''
f(x) = 1 en 0<x<b/2
f(x) = 0 en b/2<x<b

mismas condiciones de frontera
'''