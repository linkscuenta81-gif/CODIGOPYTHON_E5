# ============================================================
# Fase 5 - Evaluacion Final POA
# Problema 5: Control de horas trabajadas por recurso humano
# Nombre: Cristian Camilo Murcia Perdomo
# Codigo: 1018455612
# Programa: Ingenieria
# Fecha: 22/05/2026
# ============================================================


def calcular_y_clasificar(horas):
    """
    Funcion que calcula el total de horas semanales
    y clasifica la jornada del recurso.
    Parametros:
        horas (list): Lista con las horas trabajadas de lunes a viernes.
    Retorna:
        tuple: (total_horas, clasificacion)
    """
    total = sum(horas)
    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estandar"
    return total, clasificacion


def ingresar_datos():
    """
    Funcion que solicita al usuario los datos de cada recurso.
    Retorna:
        matriz (list): Lista de listas con nombre y horas por dia.
    """
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    matriz = []

    print("=" * 55)
    print("   INGRESO DE DATOS DE HORAS TRABAJADAS POR RECURSO")
    print("=" * 55)

    n = int(input("Ingrese el numero de recursos a registrar (minimo 4): "))
    while n < 4:
        print("Debe ingresar al menos 4 recursos.")
        n = int(input("Ingrese el numero de recursos a registrar (minimo 4): "))

    for i in range(n):
        print(f"\n--- Recurso {i + 1} ---")
        nombre = input("Nombre del recurso: ")
        horas = []
        for dia in dias:
            hora = float(input(f"Horas trabajadas el {dia}: "))
            horas.append(hora)
        matriz.append([nombre] + horas)

    return matriz


def mostrar_informe(matriz):
    """
    Funcion que recorre la matriz y genera el informe de jornadas.
    Parametros:
        matriz (list): Lista de listas con nombre y horas por dia.
    """
    print("\n" + "=" * 55)
    print("     INFORME DE HORAS TRABAJADAS POR RECURSO")
    print("=" * 55)
    print(f"{'Nombre':<20} {'Total Horas':<15} {'Clasificacion'}")
    print("-" * 55)

    for recurso in matriz:
        nombre = recurso[0]
        horas = recurso[1:]
        total, clasificacion = calcular_y_clasificar(horas)
        print(f"{nombre:<20} {total:<15} {clasificacion}")

    print("=" * 55)
    print("\n--- Informacion del estudiante ---")
    print("Nombre:   Cristian Camilo Murcia Perdomo")
    print("Codigo:   1018455612")
    print("Programa: Ingenieria")
    print("Fecha:    22/05/2026")
    print("=" * 55)
    input("\nPresione ENTER para salir...")


# -------------------------------------------------------
# Ejecucion principal
# -------------------------------------------------------
datos = ingresar_datos()
mostrar_informe(datos)