# EDP ELÍPTICA MÉTODO REGRESIVO
# EDP ELÍPTICA CUANDO TIENE LAS DOS DERIVADAS DOBLES

import numpy as np
# a, b, c y d son las esquinas de la malla
a = int(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
d = float(input("Ingrese el valor de d: "))
# Los límites de i y j
N = int(input("Ingrese el valor de N: "))
M = int(input("Ingrese el valor de M: "))


# Los pasos de i y j
h = (b-a)/N
k = (d-c)/M


# Inicializar la matriz
w = np.zeros((N+1, M+1))

# Defino la funcion
def funcion(x):
    # las x = a + h*i y las y = c + k*j
    return 10*x*(1-x)

# Condiciones de frontera
for i in range(1, N):
    w[i][0] = funcion(a+ i*h)
    w[i][M] = -5
    
for j in range(1, M):
    w[0][j] = 5*(k*j + c)
    w[N][j] = 5*np.sin((k*j + c)*np.pi*2)
    
#recorremos los puntos interiores de la malla
for rana in range(100): # iteramos 100 veces. de momento, luego pondremos condiciones de parada
    for i in range(1, N):
        for j in range(1, M):
            w[i][j] = ((k*j -1)*(w[i+1][j] + w[i-1][j]) - ((h**3*i/k**2)*(w[i][j+1] + w[i][j-1])))/(2*(k*j-1)-(2*h**3*i/k**2))
            #w[i][j] = ((k/h**2)*(w[i+1][j] + w[i-1][j]) + (1+h*i)*w[i][j-1])/(1+h*i+2*(k/h**2) -k*h*i)
            #w[i][j] = ((k/h**2)*(w[i+1][j] + w[i-1][j]) + (1+h*i)*w[i][j-1])/(1+h*i+2*(k/h**2))
            #w[i][j] = (2*k**2*(w[i+1][j] + w[i-1][j]) + h*k*(w[i+1][j+1] + w[i-1][j-1] - w[i+1][j-1] - w[i-1][j+1]) + 2*h**2*(w[i][j+1] + w[i][j-1]))/(4*(h**2 + k**2))
            #w[i][j] = (4*k**2*(w[i+1][j] + w[i-1][j]) + h*k*(w[i+1][j+1] + w[i-1][j-1] - w[i+1][j-1] - w[i-1][j+1]) + 4*h**2*(w[i][j+1] + w[i][j-1]))/(8*(h**2 + k**2))
            #w[i][j] = (4*k*(w[i+1][j] + w[i-1][j]) + (w[i+1][j+1] + w[i-1][j-1] - w[i+1][j-1] - w[i-1][j+1])*h)/(8*k)
            #w[i][j] = (k**2 * (w[i+1][j] + w[i-1][j]) + h**2 * (w[i][j+1] + w[i][j-1]) - h**2 * k**2 * funcion(i, j)) / (2*(h**2 + k**2))
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
            
'''Ejemplo 1: laplaciano. La A es el gradiente.
Au = 0  0<x<1, 0<y<1
u(0,y) = u(x,0) = u(x, 1) = 0
u(1, y) = 1'''

'''Ejemplo 2: 
Au = 0
u(x, 0) = 0, u(x, 1) = x**2
u(0, y) = 1 -y**2, u(1, y) = 1'''

'''Ejemplo 3:
Au = 2u
u(0, y)= u(x, 0) = u(x, 1) = 0
u(1, y) = 1'''#el señor dice que la u es la w, y que entomces en la f tenemos que poner w y la w original hay que cambiarla 

# el laplaciano es la divergencia del gradiente. el gradiente es el triangulo para abajo. osea que la A = traángulo al cuadrado
#nos va a preguntar por un análisis de la gráfica
# el laplaciano minimiza la energia. es como cuando una lona en tensión cae por su propio peso, hace que la tension sea la minima 