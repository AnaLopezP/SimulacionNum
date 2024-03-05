import numpy as np
# a, b, c y d son las esquinas de la malla
a = 0
b = int(input("Ingrese el valor de b: "))
b = np.pi
c = 0
d = int(input("Ingrese el valor de d: "))
d = np.pi
# Los límites de i y j
N = int(input("Ingrese el valor de N: "))
M = int(input("Ingrese el valor de M: "))
v = int(input("Ingrese el valor de v (velocidad): "))


# Los pasos de i y j
h = (b-a)/N
k = (d-c)/M
p = v*k/h

# Inicializar la matriz
w = [[0 for j in range(M+1)] for i in range(N+1)]

# Defino las funciones (nos las da el profe al principio de cada ejercicio)
def f(x):
    # las x = a + h*i y las y = c + k*j
    return 0

def g(x):
    return 0

# Condiciones de frontera
for i in range(1, N):
    w[0][i] = f(h*i)
    w[1][i] = w[0][1] + k*g(h*i)
    
for j in range(1, M):
    w[j][0] = 0
    w[j][N] = 0
    
#recorremos los puntos interiores de la malla
for i in range(1, N):
    for j in range(1, M):
        w[j+1][i] = 2*(1-p**2)*w[j][i] - w[j-1][i] + p**2*(w[j][i+1] + w[j][i-1])
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

# Convierte la lista w en un array de NumPy
Z = np.array(w)

# Grafica la función Z como una superficie en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Etiqueta los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Muestra la gráfica
plt.show()
            

# el laplaciano es la divergencia del gradiente. el gradiente es el triangulo para abajo. osea que la A = traángulo al cuadrado
#nos va a preguntar por un análisis de la gráfica
# el laplaciano minimiza la energia. es como cuando una lona en tensión cae por su propio peso, hace que la tension sea la minima 