# Función para calcular el área del triángulo
def calcular_area(lado, altura):
    # Calculamos el área usando la fórmula del área del triángulo: 0.5 * base * altura
    area = 0.5 * lado * altura
    return area

# Función para calcular la base del triángulo
def calcular_base(lado, altura):
    # Calculamos la base usando el teorema de Pitágoras: base = √(lado^2 - altura^2)
    base = (lado**2 - altura**2)**0.5
    return base

# Función principal
def main():
    lado = float(input("Ingrese la medida de un lado del triángulo: "))  # Solicita la medida de un lado al usuario
    altura = float(input("Ingrese la altura relativa al lado dado: "))  # Solicita la altura relativa al lado dado al usuario

    # Calculamos la base del triángulo
    base = calcular_base(lado, altura)

    # Calculamos el área del triángulo
    area = calcular_area(base, altura)

    print("El área del triángulo es:", area)  # Imprime el resultado

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()  # Llama a la función principal si es así

"""
Sí, se puede utilizar el algoritmo para calcular el área de un triángulo rectángulo si se dan las medidas de sus dos lados perpendiculares. 
En este caso, uno de los lados perpendiculares se consideraría la base del triángulo y el otro lado perpendicular sería la altura relativa a esta base. 
Por lo tanto, podríamos utilizar el mismo algoritmo con algunos ajustes menores.

"""