# SimulacionNum

En el examen tenemos que hacer todos los pasos. Él nos dice si son progresivos o regresivos, pero nosotros lo ponemos en funcion de w y despejamos el que toque.

En regresivo despejamos wij
En progresivo despejamos wij+1

No tenemos en cuenta el error

Siempre que sea regresiva lo hacemos como un sistema lienal es decir, al pasar to do a w, podemos tratar como un sistema lineal, donde se resolverian con otro bucle las w

Met de gauss-seiden lo que hace es iterar el sistema lineal, hallando wij. 
El otro método es el de evolución, que lo que hace es tomar los valores anteriores (los de abajo de la malla) y halla el valor de wij+1. 

Si no dice nada podemos usar el método que nos salga. 