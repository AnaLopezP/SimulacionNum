import numpy as np

# a, b, c y d son las esquinas de la malla
b = int(input("Ingrese el valor de b: "))
d = int(input("Ingrese el valor de d: "))
# Los límites de i y j
N = int(input("Ingrese el valor de N: "))
M = int(input("Ingrese el valor de M: "))
v = float(input("Ingrese el valor de v (conductividad): ")) #creo que es el alfa

# Los pasos de i y j
h = b/N
k = d/M
lam = (k/h**2)*v**2

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
    
for l in range(100):
    for j in range(0, M):
        for i in range(1, N):
            w[i][j] = (lam*(w[i][j+1] + w[i][j-1]) + w[i][j-1])/1+2*lam
            
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
            