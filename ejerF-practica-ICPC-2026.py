def main():
    # APRENDIENDO SOBRE LA CARGA 
    #Leer cada linea de entrada y procesarla utilizando la libreria sys que permite leer de la entrada estándar
    #Leemos la primer linea con la funcion sys.stdin.readline() y la convertimos a entero, esta conversion es necesaria
    #para poder utilizar el valor de N en los bucles posteriores 
    #Lo que hace la instrucciones igualadas a sys.stdin.readline() y devolverla como una cadena de texto, luego se utiliza el método strip() para eliminar cualquier espacio en blanco al inicio o al final de la cadena 
    # y finalmente se convierte a entero con int().
    # Implica leer la entrada estándar, sys es la librería que permite leer de la entrada estándar, 
    # y stdin es el flujo de entrada estándar, readline() lee una línea completa de la entrada estándar.
    #  Para casos que se quiera ingresar una lista de valores separados con espacios, como por ejemplo los tiros
    # se puede utilizar la función split() para dividir la cadena en una lista de subcadenas, es decir sin ingresar los datos sin [] para representar la lista, 
    # utilizo luego map() para convertir cada subcadena a un entero.
    # entonces cada elemento que era un string debido a la funcion split() se convierte a entero gracias a la funcion map() que aplica la funcion int() a cada elemento de la lista.
    
    import sys
    def main():
        N=int(sys.stdin.readline().strip()) 
        #line2 contiene en las primeras dos posiciones W y L que definen ancho y altura de la cuadricula,que no se utilizan, y en las posiciones 2 y 3 Tx y Ty valores de las coordenadas del objetivo
        line2=sys.stdin.readline().split()  #ahora line2 es una lista de strings
        Tx=int(line2[2]) #convertimos a entero la coordenada x del objetivo para luego calcular la distancia de cada tiro a este objetivo
        Ty=int(line2[3]) 
        distA=[] #vector que almacena las distancia de cada tiro del equipo Azul al objetivo
        distR=[]
        for i in range(N):
            x,y=map(int,sys.stdin.readline().split()) #leemos las coordenadas de cada tiro y las convertimos a enteros, primero se leyo la coordenada de x y luego la de y, se hace esto para el equipo A. Si se hubiese puesto list(map(int,sys.stdin.readline().split())) se hubiese creado una lista de enteros, pero no es necesario ya que solo necesitamos las coordenadas para calcular la distancia al objetivo.
            dx=x-Tx #diferencia en x entre el tiro y el objetivo
            dy=y-Ty #diferencia en y entre el tiro y el objetivo
            distA.append(dx*dx+dy*dy) #distancia al cuadrado del tiro al objetivo, sin sqrt para evitar la raiz cuadrada innecesaria (menos costo comp)

        for i in range(N):
            x,y=map(int,sys.stdin.readline().split())
            dx=x-Tx
            dy=y-Ty
            distR.append(dx*dx+dy*dy)

            minA=min(distA) #minima distancia del tiro del equipo A al objetivo
            minR=min(distR) #minima distancia del tiro del equipo R al objetivo
            points=0 #inicializamos el contador de puntos del equipo A
            if(minA<minR): #si la minima distancia del equipo A es menor que la minima distancia del equipo R, entonces el equipo A gana
                for actualA in distA: #recorremos cada tiro del equipo A
                    if(actualA,minR):
                        points=+1
                print("A",points) #imprimimos el resultado del equipo A
            else:
                for actualR in distR:
                    if(actualR<minA):
                        points=+1
                print("R",points) #imprimimos el resultado del equipo R

    if __name__ == '__main__':
        main()



            


