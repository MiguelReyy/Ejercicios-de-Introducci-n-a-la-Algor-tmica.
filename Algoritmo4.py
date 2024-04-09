# Función para calcular la media ponderada
def calcular_media_ponderada(nums, pnds):
    # Verificar que las listas tengan la misma longitud
    if len(nums) != len(pnds):
        return "Error: las listas deben tener la misma longitud"

    # Calcular la suma de los productos de los números y sus ponderaciones
    suma_productos = sum([num * ponder for num, ponder in zip(nums, pnds)])

    # Calcular la suma de los coeficientes de ponderación
    suma_ponderaciones = sum(pnds)

    # Calcular la media ponderada
    media_ponderada = suma_productos / suma_ponderaciones

    return media_ponderada

# Función principal
def main():
    nums = []
    pnds = []

    # Solicitar al usuario que ingrese los números y sus ponderaciones
    n = int(input("Ingrese la cantidad de números: "))
    for i in range(n):
        nums.append(float(input(f"Ingrese el número {i + 1}: ")))
        pnds.append(float(input(f"Ingrese la ponderación para el número {i + 1}: ")))

    # Calcular la media ponderada
    media = calcular_media_ponderada(nums, pnds)

    # Mostrar el resultado
    if isinstance(media, str):
        print(media)
    else:
        print("La media ponderada es:", media)

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()  # Llama a la función principal si es así
