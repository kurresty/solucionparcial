BONIFICACION_DIRECTIVO_ALTO = 0.20
BONIFICACION_DIRECTIVO_MEDIO = 0.15
BONIFICACION_OPERATIVO_ALTO = 0.10
BONIFICACION_OPERATIVO_MEDIO = 0.5

def calcular_bonificacion(salario_base, cargo, desempeno):

    #Determinaar la bonificacion segun el cargo y el nivel de desempeño


    if cargo == 'directivo':
        if desempeno == 'alto':
            bonificacion = salario_base * BONIFICACION_DIRECTIVO_ALTO
        elif desempeno == 'medio':
            bonificacion = salario_base * BONIFICACION_DIRECTIVO_MEDIO
        else:
            bonificacion = 0
    elif cargo == 'operativo':
        if desempeno == 'alto':
            bonificacion = salario_base * BONIFICACION_OPERATIVO_ALTO
        elif desempeno == 'medio':
            bonificacion = salario_base *  BONIFICACION_OPERATIVO_MEDIO

        else:
            bonificacion = 0;
    else:
        bonificacion = 0


    return bonificacion

#funcion para calcular el total a recibir (salario base + bonificacion)
def calcular_total(salario_base, bonificacion):
    return salario_base + bonificacion

def mostrar_resumen(salario_base, cargo, desempeno, bonificacion, total):

    print(f"-----Resumen del pago-----")
    print(f"Cargo: {cargo.capitalize()}")
    print(f"Nivel de Desempeño: {desempeno.capitalize()}")
    print(f"Salario Base: ${salario_base:.0f}")
    print(f"Bonificacion: ${bonificacion:.0f}")
    print(f"Total a Recibir: ${total:.0f}")
    print("---------------------------\n")

#Entradas

salario_base = float(input("Ingrese el Salario Base: $"))
cargo = input("Inglese el Cargo empleado (directivo7operativo): ").lower()
desempeno = input("Ingrese el Nivel de desempeño (alto/medio/bajo): ").lower()


#calcular_bonificacion
bonificacion = calcular_bonificacion(cargo, desempeno, salario_base)

#calcular total a recibir
total = calcular_total(salario_base, bonificacion)

#invocamos la funcion
mostrar_resumen(cargo, desempeno, salario_base, bonificacion, total)