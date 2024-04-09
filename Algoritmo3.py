# Función para calcular la media aritmética
def calcular_media(num1, num2, num3):
    media = (num1 + num2 + num3) / 3  # Calcula la media aritmética
    return media

# Función principal
def main():
    num1 = float(input("Ingrese el primer número: "))  # Solicita el primer número al usuario
    num2 = float(input("Ingrese el segundo número: "))  # Solicita el segundo número al usuario
    num3 = float(input("Ingrese el tercer número: "))  # Solicita el tercer número al usuario

    media = calcular_media(num1, num2, num3)  # Calcula la media usando la función calcular_media

    print("La media aritmética de los tres números es:", media)  # Imprime el resultado

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()  # Llama a la función principal si es así
