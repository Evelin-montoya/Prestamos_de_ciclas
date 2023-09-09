# listas vacías 
personas = []  #información de la persona
prestamos_bicicletas = []  # información de préstamos

#registrar un usuario
def registrar_persona():
    nombre = input("Ingrese el nombre de la persona que se va a registrar: ")
    numero_tarjeta = input("Ingrese el número de tarjeta para prestar una biciclta: ")
    
    personas.append([nombre, numero_tarjeta]) # intersede los datos a lista de personas
    
    print(f"Persona registrada: Nombre {nombre} ~ Tarjeta: {numero_tarjeta}")# Aca confirmamos el registro de la persona

# tomar una bicicleta
def prestar_bicicleta():
    
    numero_tarjeta = input("Inserte el número de tarjeta de la persona resgistrada: ")
    origen = input("Inserte el origen del préstamo: ")
    destino = input("Inserte el destino del préstamo: ")

    usuario_encontrado = False
    
    for usuario in personas: # busca la persona en la lista de usuarios por su número de tarjeta
        if usuario[1] == numero_tarjeta:
            usuario_encontrado = True
            break

    if usuario_encontrado:
        prestamos_bicicletas.append([numero_tarjeta, origen, destino])# agrega la información del préstamo a la lista de préstamos
        print(f"La persona con número de tarjeta {numero_tarjeta} ha prestado una bicicleta \ndesde {origen} \nhasta {destino}")# mensaje confirmando el préstamo de la bicicleta
    else:
        print(f"La persona con número de tarjeta {numero_tarjeta} no ha sido encontrado")# Aca hay un mensaje po  si el usuario no se encuentra en la lista

def devolver_bicicleta():
            numero_tarjeta = input("Inserte el número de tarjeta de la persona: ")
            usuario_encontrado = False

            for prestamo in prestamos_bicicletas:
                if prestamo[0] == numero_tarjeta:
                    usuario_encontrado = True
                    prestamo.append("Devuelto")
                    print(f"La persona con número de tarjeta {numero_tarjeta} ha devuelto la bicicleta.")
                    break

            if not usuario_encontrado:
                print(f"La persona con número de tarjeta {numero_tarjeta} no tiene una bicicleta prestada.")


# Aca podemos consultar las personas que se han resgistrado
def consultar_usuarios():
    print("Listado de personas:")
    for usuario in personas: #imprime nombre y numero
        print(f"Nombre: {usuario[0]}, Tarjeta: {usuario[1]}")

# Aca podemos consultar el numeor de resptamos que hemos hecho de las bocicletas 
def consultar_prestamos():
    print("Listado de Préstamos:")
    for prestamo in prestamos_bicicletas:
        print(f"Tarjeta: {prestamo[0]}, Origen: {prestamo[1]}, Destino: {prestamo[2]}")

# Menú principal
while True:
    print("\n ----Menú Principal---- ")
    print("1. Registrar persona")
    print("2. Prestar bicicleta")
    print("3. Consultar Listado de personas")
    print("4. Consultar Listado de préstamos")
    print("5. Devolver prestamo de bicicleta")
    print("6. Salir")

    opcion = input("Seleccione una opción del 1 al 6: ")

    if opcion == "1":
        registrar_persona()
    elif opcion == "2":
        prestar_bicicleta()
    elif opcion == "3":
        consultar_usuarios()
    elif opcion == "4":
        consultar_prestamos()
    elif opcion == "5":
        devolver_bicicleta()
    elif opcion == "6":
        print("¡Has seleccionado la opcion salir. Ten un excelente dia!")
        break
    else:
        print("Esta opcion no es valida. Selleciona otra opcion que si lo sea .")