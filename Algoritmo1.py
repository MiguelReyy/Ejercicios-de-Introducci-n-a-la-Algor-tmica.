# Función para calcular el precio con impuestos
def calcular_precio_con_impuestos(precio, iva):
    precio_con_impuestos = precio * (1 + iva / 100)  # Calcula el precio con impuestos
    return precio_con_impuestos

# Función principal
def main():
    precio = float(input("Ingrese el precio sin impuestos: "))  # Pide al usuario que ingrese el precio sin impuestos
    iva = float(input("Ingrese el porcentaje de IVA: "))  # Pide al usuario que ingrese el porcentaje de IVA

    precio_con_impuestos = calcular_precio_con_impuestos(precio, iva)  # Calcula el precio con impuestos

    print("El precio con impuestos incluidos es:", precio_con_impuestos)  # Imprime el resultado

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()  # Llama a la función principal si es así
