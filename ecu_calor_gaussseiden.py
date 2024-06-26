# ESTO ES DIFERENCIA REGRESIVA 
# En las regresivas despejamos wi, j mientras que en las progresivas despejamos w i j+1
# LAS ECUACIONES DE CALOR SON EDP PARABÓLICAS
import numpy as np

# a, b, c y d son las esquinas de la malla
b = int(input("Ingrese el valor de b: ")) #x
d = int(input("Ingrese el valor de d: ")) #t
# Los límites de i y j
N = int(input("Ingrese el valor de N: "))
M = int(input("Ingrese el valor de M: "))
v = float(input("Ingrese el valor de v (conductividad): ")) #alfa (tiene que ser menor que el máximo formula en el cuad)

# Los pasos de i y j
h = b/N
k = d/M
lam = (k/h**2)*v**2

w = np.zeros((N+1, M+1))

def f(x):
    return np.exp(-(x-b/2)**2)

# Condiciones de frontera
for i in range(1, N):
    w[i][0] = f(i*h)
    w[i][1] = 0
    
for j in range(1, M):
    w[0][j] = 0
    w[N][j] = 0
    
for l in range(100):
    for j in range(1, M):
        for i in range(1, N):
           # base w[i][j] = (lam*(w[i][j+1] + w[i][j-1]) + w[i][j-1])/(1+2*lam)
           # ejercicio 1 w[i][j] = ((k/h**2)*(w[i+1][j] + w[i-1][j]) + (1+h*i)*w[i][j-1])/(1+h*i+2*(k/h**2))
           # ejercicio 2 w[i][j] = (k*(w[i+1][j] + w[i-1][j]) + h**2*(1+h*i)*w[i][j-1])/(2*k-k*h**2+h**2*(1+h*i))
           # ejercicio 2 abril
           
           w[i][j] = (-k*(w[i+1][j] + w[i-1][j]) - h**2*(1+h*i)*w[i][j-1])/(-2*k+k*h**3*i-h**2*(1+h*i))
            
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

'''Ejercicio 1
f(x) = e^(-(x-b/2)^2)
b= 5
d = 10
N= 40
M = 400
0.2 <v < 1.5'''

'''
Ejercicio cuaderno dia 20/03. 
Por culpa del (1+x), la gráfica se tuerce para un lado al bajar el calor
'''