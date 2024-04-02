# SimulacionNum

En el examen tenemos que hacer todos los pasos. Él nos dice si son progresivos o regresivos, pero nosotros lo ponemos en funcion de w y despejamos el que toque.

En regresivo despejamos wij
En progresivo despejamos wij+1

No tenemos en cuenta el error

Cuando es progresiva, solo se resuelve la ecuacion en un bucle, ya que hayas los puntos posteriores en base a los anteriores. No hay sistema lineal en el que iterar.
Siempre que sea regresiva lo hacemos como un sistema lienal es decir, al pasar to do a w, podemos tratar como un sistema lineal, donde se resolverian con otro bucle las w

Met de gauss-seiden lo que hace es iterar el sistema lineal, hallando wij. 
El otro método es el de evolución, que lo que hace es tomar los valores anteriores (los de abajo de la malla) y halla el valor de wij+1. 

Si no dice nada podemos usar el método que nos salga. 

Tambien hay que calcular las característcas.

El método de evolucion se usa para las edp hiperbólicas y algunas parabólicas.


1) Nos dan una EDP no está en forma canónica --> tenemos que discretizar las derivadas parciales
2) Aproximamos las derivadas --> sustituimos las aproximaciones en la EDP y despejamos la primera derivada parcial
3) Discretizamos la EDP --> despejamos wij o wij+1 según lo que queramos (diferencias progresivas o diferencias regresivas)
4) Si hemos usado diferencias regresivas, el paso ahora es negativo, porque evaluamos en i,j lo que vale i, j-1. En la primera derivada da igual cual de las dos opciones usemos.
5) Tenemos que resolver la ecuacion, para lo que tenemos 2 métodos: sistema de gauss seiden o metodo de evolucion. El primero es el de las 100 iteraciones, que resuelve un sistema lineal, mientras que el de evolucion es el otro, en el que despejas wij. (Hallamos los valores posteriores con los anteriores)

¿cómo se resuelve un sistema lineal por gauss-seiden?
hay una ecuacion para cada punto de la malla, en cada punto intervienen distintos valores. Hay una incognita y ecuacion por cada punto de la malla. Al ser un sistema lineal, podemos ponerlo en forma matricial y hace cosas con las matrices (triangulacion, creo)