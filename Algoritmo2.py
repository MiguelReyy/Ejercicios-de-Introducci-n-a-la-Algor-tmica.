# Función para calcular los intereses
def calcular_intereses(capital, tasa, tiempo):
    intereses = (capital * tasa / 100) * tiempo  # Calcula los intereses
    return intereses

# Función principal
def main():
    capital = float(input("Ingrese el capital invertido: "))  # Solicita el capital invertido al usuario
    tasa = float(input("Ingrese la tasa de interés (%): "))  # Solicita la tasa de interés al usuario
    tiempo = int(input("Ingrese el tiempo en meses: "))  # Solicita el tiempo en meses al usuario

    intereses = calcular_intereses(capital, tasa, tiempo)  # Calcula los intereses usando la función calcular_intereses

    print(f"El importe de los intereses generados es: {intereses} €")  # Imprime el resultado

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()  # Llama a la función principal si es así
