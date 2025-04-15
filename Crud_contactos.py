menu = {
    '1' : "Agregar Contacto",
    '2' : "Ver contacto",
    '3' : "Actualizar contacto",
    '4' : "Eliminar Contacto",
    '5' : "Salir"
}

contactos = {}

proximo_id = 1

def mostrar_menu(menu):
    print("\nAgenda de Contactos\n")
    for key, (nombre) in menu.items():
        print(f"{key}, {nombre}")

    opcion = input("\nElije una opcion (1-5): ")
    return opcion

def agregar_contacto():
    global proximo_id

    print("\nAgregar contacto 😃")
    nombre = input("\nNombre: ").strip()
    telefono = input("Telefono: ").strip()
    correo = input("Correo: ").strip()
    direccion = input("Direccion: ").strip()
    comentarios = input("Comentarios: ").strip()
    
    if not nombre or not telefono:
        print("❌ El nombre y telefono son obligatorios")
        return
    
    nuevo_contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion,
        "comentarios": comentarios
    }

    contactos[proximo_id] = nuevo_contacto
    print(f"\n✅ Contacto agregado con ID {proximo_id}")

    proximo_id += 1

def ver_contacto():
    if not contactos:
        print("\nNo hay contactos guardados")
        return
    
    print("\nLista de Contactos")
    for id, info in contactos.items():
        print(f"\nID: {id}")
        for campo, valor in info.items():
            print(f" {campo.capitalize()}: {valor}")

def actualizar_contacto():
    entrada_id = input("Ingresa el ID del contacto que deseas actualizar: ")

    if not entrada_id.isdigit():
        print("Error, ingresa un numero valido")
        return
    
    id_int = int(entrada_id)

    if id_int not in contactos:
        print("❌ ID no encontrado")
        return

    contacto = contactos[id_int]

    actualizado = False
    for campo, valor_actual in contacto.items():
        nuevo_valor = input(f"\n{campo.capitalize()} actual: {valor_actual} \nNuevo {campo} (deja vacio para mantener): ").strip()

        if nuevo_valor:
            contacto[campo] = nuevo_valor
            actualizado = True

    if actualizado:
        print("✅ Contacto Actualizado Correctamente")
    else:
        print("No se realizaron cambios")


def eliminar_contacto():
    entrada_id = input("Ingresa el ID del contacto a eliminar: ")

    if not entrada_id.isdigit():
        print("Error, ingresa un numero valido")
        return
    
    id_int = int(entrada_id)

    if id_int not in contactos:
        print("ID no encontrado")
        return
    
    print(contactos[id_int])

    confirmar_eliminar = input("¿Seguro quieres eliminar este contacto? (s/n): ").strip().lower()

    if confirmar_eliminar == "s":
        del contactos[id_int]
        print("✅ Contacto eliminado correctamente")
    else:
        print("❌ Eliminacion Cancelada")

def confirmar_salida():
    respuesta = input("¿Seguro que quieres salir? (s/n): ").strip().lower()
    return respuesta == "s"

def main():
    while True:
    
        opcion = mostrar_menu(menu)

        if opcion == "1":
            agregar_contacto()

        elif opcion == "2":
            ver_contacto()

        elif opcion == "3":
            actualizar_contacto()
        
        elif opcion == "4":
            eliminar_contacto()
        
        else:
            if confirmar_salida():
                print("\n👋🏽 Hasta luego\n")
                break
            continue

if __name__ == "__main__":
    main()