import json

def mostrar_menu():
    print("=== GESTION DE RESERVAS CANCHA F5 ===")
    print("1 Registrar reserva")
    print("2 Consultar reservas")
    print("3 Modificar datos de reserva")
    print("4 Cancelar reserva")
    print("5 Buscar reservas por nombre")
    print("0 Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


def registrar_reserva(lista):
    import colorama
    print("=== REGISTRAR RESERVA ===")

    nombre = validar_no_vacios(input("Ingrese el nombre del cliente: "))
    fecha = validar_no_vacios(input("Ingrese la fecha de la reserva (dd/mm/aaaa): "))
    hora = validar_no_vacios(input("Ingrese la hora de la reserva (hh:mm): "))
    deporte = validar_no_vacios(input("Ingrese el tipo de actividad: "))

    # Validar superposición
    while not evitar_superposicion_dia_hora(lista, fecha, hora):
        colorama.init()
        print(colorama.Fore.RED + "Ya existe una reserva para esa fecha y hora." + colorama.Style.RESET_ALL)
        fecha = validar_no_vacios(input("Ingrese una fecha válida: "))
        hora = validar_no_vacios(input("Ingrese una hora válida: "))

    reserva = {
        "id": len(lista) + 1,
        "nombre": nombre,
        "fecha": fecha,
        "hora": hora,
        "deporte": deporte,
        "estado": "activo",
    }

    lista.append(reserva)
    print("Reserva registrada con éxito!")


def validar_no_vacios(dato):
    import colorama

    if dato == "":
        colorama.init()
        print(colorama.Fore.RED + "El dato no puede estar vacío!" + colorama.Style.RESET_ALL)
        while True:
            dato = input("Ingrese un dato válido: ")
            if dato != "":
                return dato

    return dato


def listar_turnos(lista: list):
    if len(lista) == 0:
        print("No hay reservas registradas")
    else:
        print("RESERVAS".center(70, "-"))
        print(f"{'id':<5}{'nombre':<15}{'fecha':<12}{'hora':<10}{'deporte':<15}{'estado':<10}")

        for reserva in lista:
            print(
                f"{reserva['id']:<5}"
                f"{reserva['nombre']:<15}"
                f"{reserva['fecha']:<12}"
                f"{reserva['hora']:<10}"
                f"{reserva['deporte']:<15}"
                f"{reserva['estado']:<10}"
            )


def modificar_reserva(lista: list):
    id = int(input("Ingrese el ID de la reserva a modificar: "))

    if verificar_existencia_reserva(lista, id):
        for reserva in lista:
            if reserva["id"] == id:
                print("Reserva encontrada!")
                print("Deje en blanco para NO modificar un campo.")

                nombre = input(f"Nombre actual ({reserva['nombre']}): ")
                fecha = input(f"Fecha actual ({reserva['fecha']}): ")
                hora = input(f"Hora actual ({reserva['hora']}): ")
                deporte = input(f"Deporte actual ({reserva['deporte']}): ")

                if nombre != "":
                    reserva["nombre"] = nombre
                if fecha != "":
                    reserva["fecha"] = fecha
                if hora != "":
                    reserva["hora"] = hora
                if deporte != "":
                    reserva["deporte"] = deporte

                print("Reserva modificada con éxito!")
                return

    else:
        print("El ID ingresado no existe!")


def verificar_existencia_reserva(lista: list, id: int):
    for reserva in lista:
        if reserva["id"] == id:
            return True
    return False


def cancelar_reserva(lista: list):
    id = int(input("Ingrese el ID de la reserva a cancelar: "))

    if verificar_existencia_reserva(lista, id):
        for reserva in lista:
            if reserva["id"] == id:
                print("=== DATOS DE LA RESERVA ===")
                print(f"Nombre: {reserva['nombre']}")
                print(f"Fecha: {reserva['fecha']}")
                print(f"Hora: {reserva['hora']}")
                print(f"Deporte: {reserva['deporte']}")

                resp = input("¿Está seguro que desea cancelar? (s/n): ")

                if resp.lower() == "s":
                    reserva["estado"] = "cancelado"
                    print("Reserva cancelada con éxito!")
                else:
                    print("Operación cancelada por el usuario.")
                return
    else:
        print("El ID ingresado no existe!")


def buscar_reservas_por_nombre(lista: list):
    nombre = validar_no_vacios(input("Ingrese el nombre a buscar: "))
    encontrados = []

    for reserva in lista:
        if reserva["nombre"].lower() == nombre.lower():
            encontrados.append(reserva)

    if len(encontrados) == 0:
        print("No se encontraron reservas con ese nombre.")
    else:
        print(f"Se encontraron {len(encontrados)} reservas:")
        print(f"{'id':<5}{'nombre':<15}{'fecha':<12}{'hora':<10}{'deporte':<15}")
        for reserva in encontrados:
            print(
                f"{reserva['id']:<5}"
                f"{reserva['nombre']:<15}"
                f"{reserva['fecha']:<12}"
                f"{reserva['hora']:<10}"
                f"{reserva['deporte']:<15}"
            )


def limpiar_pantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")


def evitar_superposicion_dia_hora(lista: list, fecha: str, hora: str):
    for reserva in lista:
        if reserva["fecha"] == fecha and reserva["hora"] == hora:
            return False
    return True


def cargar_datos():
    try:
        with open("reserva.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def guardar_datos(lista):
    with open("reserva.json", "w") as archivo:
        json.dump(lista, archivo, indent=4)
