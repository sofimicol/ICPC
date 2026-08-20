import sys 
def main():
    N,M= map(int, sys.stdin.readline().split())
    cantAlfajoresXViaje=list(map(int, sys.stdin.readline().split()))
    cantEmpleados=list(map(int, sys.stdin.readline().split()))
    # Idea: primero me paro en la posicion 0 de cantAlfajoresXViaje y recorro la lista de empleados para hacer la resta entre
    # el elemento en la posicion 0 de cantAlfajoresXViaje y el elemento en la posicion 0 de cantEmpleados
    # Si resta es menor que cero entonces no se reparte nada y paso a la posicion siguiente del vector cantEmpleados
    # Si la cant de la posicion siguiente es menor o igual a la cantidad de alfajores para cada viaje, entonces los resto y decremento el valor de 
    # la cant de cantAlfajoresXViaje siendo este la resta entre cantAlfajoresXViaje y cantEmpleados
    # Teniendo en cuenta que Seba reparte la mayor cantidad posible de alfajores a cada oficina y que en cada viaje comienza desde la primera*/
    
    for i in range(N):
        for j in range (M):
            cantAlfajoresXViaje[i]%=cantEmpleados[j] #Al principio pense en la verificar que el numero de CantAlfajoresXViaje sea mayor o igual que cantEmpleados, pero si no es asi la funcion resto igual lo contempla

    print(cantAlfajoresXViaje)

if __name__ == '__main__':
            main()
