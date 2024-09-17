def encontrar_inferior_superior(lista, numero):
    inferior = None
    superior = None
    
    # Buscar el número inferior
    for num in lista:
        if num < numero:
            inferior = num
        if num > numero:
            superior = num
            break
    
    # Si no hay un número inferior o superior, devolver 'X'
    return (inferior if inferior is not None else 'X', superior if superior is not None else 'X')

def ingresar_lista():
    # 1) Ingresar el tamaño de la lista de números a evaluar
    n = int(input("Ingrese el tamaño de la lista: "))
    
    # 2) Ingresar la lista de números separados por espacios
    lista = list(map(int, input(f"Ingrese {n} números enteros separados por espacio: ").split()))
    
    # Ordenar la lista antes de retornarla
    lista.sort()
    
    return lista

def realizar_consultas(lista):
    # 3) Ingresar el número de consultas a evaluar
    m = int(input("Ingrese el número de consultas: "))
    
    while True:
        # 4) Ingresar la lista de números a consultar
        consultas = list(map(int, input(f"Ingrese {m} números a consultar separados por espacio: ").split()))
        
        # Validar que las consultas no sean mayores que el último número de la lista
        if max(consultas) > lista[-1]:
            print(f"Error: El número de consulta {max(consultas)} excede el valor máximo de la lista {lista[-1]}. Intente nuevamente.")
        else:
            # Procesar cada consulta
            for consulta in consultas:
                inferior, superior = encontrar_inferior_superior(lista, consulta)
                print(f'Consulta: {consulta}, Inferior: {inferior}, Superior: {superior}')
            break  # Salir del ciclo una vez que todas las consultas sean válidas

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Ingresar nueva lista de números")
    print("2. Realizar consultas")
    print("3. Mostrar lista actual")
    print("4. Salir")

def main():
    lista = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            # Opción para ingresar una nueva lista
            lista = ingresar_lista()
            print("Lista ingresada correctamente.")
        
        elif opcion == '2':
            # Opción para realizar consultas si ya hay una lista ingresada
            if lista:
                realizar_consultas(lista)
            else:
                print("Primero debe ingresar una lista de números (opción 1).")
        
        elif opcion == '3':
            # Mostrar la lista actual
            if lista:
                print(f"Lista actual: {lista}")
            else:
                print("No se ha ingresado ninguna lista.")
        
        elif opcion == '4':
            # Opción para salir del programa
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
