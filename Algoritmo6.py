# Función para calcular la tarifa por hora normal
def calcular_tarifa_normal(salario_bruto_mensual):
    salario_bruto_anual = salario_bruto_mensual * 12
    salario_bruto_semanal = salario_bruto_anual / 52
    tarifa_hora_normal = salario_bruto_semanal / 40  # Cambiar de 35 a 40 horas semanales
    return tarifa_hora_normal

# Función para calcular el importe de las horas extra
def calcular_importe_horas_extra(horas_extra, tarifa_normal):
    importe_horas_extra = 0

    # Calculamos el importe de las horas extra
    if horas_extra <= 40:  # No hay horas extra
        importe_horas_extra = 0
    elif horas_extra <= 48:  # Horas extra entre la 41ª y la 48ª
        horas_extra_normales = horas_extra - 40
        importe_horas_extra = horas_extra_normales * (tarifa_normal * 1.25)
    else:  # Horas extra a partir de la 49ª
        horas_extra_normales = 48 - 40
        importe_horas_extra += horas_extra_normales * (tarifa_normal * 1.25)
        horas_extra_extra = horas_extra - 48
        importe_horas_extra += horas_extra_extra * (tarifa_normal * 1.5)

    return importe_horas_extra

# Función principal
def main():
    salario_bruto_mensual = float(input("Ingrese el salario mensual bruto: "))  # Solicita el salario bruto mensual al usuario
    horas_extra = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))  # Solicita la cantidad de horas extra al usuario

    tarifa_normal = calcular_tarifa_normal(salario_bruto_mensual)
    importe_horas_extra = calcular_importe_horas_extra(horas_extra, tarifa_normal)

    print("El importe de las horas extra a pagar es:", importe_horas_extra)  # Imprime el resultado

# Verifica si el script se está ejecutando directamente
if __name__ == "__main__":
    main()  # Llama a la función principal si es así
