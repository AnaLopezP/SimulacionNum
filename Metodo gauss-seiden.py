# a, b, c y d son las esquinas de la malla
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
d = float(input("Ingrese el valor de d: "))
# Los límites de i y j
N = float(input("Ingrese el valor de N: "))
M = float(input("Ingrese el valor de M: "))

# Los pasos de i y j
h = b-a/N
k = d-c/M

# Inicializar la matriz
w = [[]]

# Creamos la matriz
for i in range(N):
    for j in range(M):
        w[i][j] = 0

def funcion(i, j):
    return None

# Condiciones de frontera
for i in range(1, N):
    w[i][0] = None
    w[i][M] = None
    
for j in range(1, M):
    w[0][j] = None
    w[N][j] = None
    
#recorremos los puntos interiores de la malla
for k in range(100): # iteramos 100 veces. de momento, luego pondremos condiciones de parada
    for i in range(1, N):
        for j in range(1, M):
            w[i][j] = (h**2+k**2)**2*(k**2*(w[i+1][j]+w[i-1][j]) + h**2*(w[i][j+1]+w[i][j-1]))/(2*(h**2+k**2)**2)