import sys 
#Ejercicio I: Iteracciones sociales
def main():
    N,M= map(int, sys.stdin.readline().split())
    gananciaOro=[0]*(N+1) 
    for i in range(M):
        X,Y=map(int,sys.stdin.readline().split())
        opciones=list(map(int,sys.stdin.readline().split()))
        cantidad1 = opciones.count(1)
        ganancia1=0
        ganancia1=X//(cantidad1+1) #suponiendo que ines elige esta opcion
        opciondeInes=0
        if(ganancia1>=Y):
            opciondeInes=1
        else:
            opciondeInes=2
            if(cantidad1!=0): #contemplar division por cero
                ganancia1=X//(cantidad1) #ines elige otra opcion
        for j in range (N):
            if(opciones[j]==1):
                gananciaOro[j]+=ganancia1
            else:
                gananciaOro[j]+=Y
        if(opciondeInes==1):
            gananciaOro[N]+=ganancia1 
        else:
            gananciaOro[N]+=Y
    print(*(gananciaOro))

if __name__ == "__main__":
    main()

