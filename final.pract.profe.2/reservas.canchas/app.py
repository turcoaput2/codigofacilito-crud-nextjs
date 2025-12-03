from funciones import (
    mostrar_menu,
    registrar_reserva,
    listar_turnos,
    modificar_reserva,
    cancelar_reserva,
    buscar_reservas_por_nombre,
    limpiar_pantalla,
    cargar_datos,
    guardar_datos
)

def main():
    reservas = cargar_datos()  # carga archivo JSON si existe

    while True:
        limpiar_pantalla()
        opcion = mostrar_menu()   # ← ESTA ES LA CORRECTA, NO mostrar_menu_menu NI leer_opcion_menu

        if opcion == "1":
            registrar_reserva(reservas)
        elif opcion == "2":
            listar_turnos(reservas)
        elif opcion == "3":
            modificar_reserva(reservas)
        elif opcion == "4":
            cancelar_reserva(reservas)
        elif opcion == "5":
            buscar_reservas_por_nombre(reservas)
        elif opcion == "0":
            guardar_datos(reservas)
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida!")

        input("\nPresione ENTER para continuar...")

if __name__ == "__main__":
    main()
