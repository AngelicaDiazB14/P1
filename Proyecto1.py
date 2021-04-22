#..................................Proyecto-Sistema de reservación de viajes..........................................#





#________________________________________MENÚ PRINCIPAL y SUB-MENÚS_________________________________________________#

"""
-Nombre: menuAdministrativo

-Entradas: un número según la opción que desee realizar el usuario y
las demás entradas van de acuerdo a la opción seleccionada.

-Salidas: el retorno de lo realizado según las opciones escogidas entre Gestión de empresas, Gestión de tranporte por
empresa, Gestión de viajes, Consultar historial de reservaciones y Salir.

-Restricciones: van según el tipo de opción escogida, además solo se puede acceder a este menú si se ingresa una clave
que ya esté registrada junto con el usuario.
"""


def menuAdministrativo():
    print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨MENÚ ADMINISTRATIVO¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨\n")
    print("  (1) Gestión de empresas\n  (2) Gestión de transporte por empresa\n  (3) Gestión de viajes\n")
    print("  (4) Consultar historial de reservaciones\n  (5) Salir\n")
    print("Por favor, introduzca el número de la operación que desea realizar: ")
    opcion = input("")
    opcion = int(opcion)
    if(opcion == 1):
        return 
    elif(opcion == 2):
        return
    elif(opcion == 3):
        return 
    elif(opcion == 4):
        return
    elif(opcion == 5):
        return menuPrincipal()
    else:
        print("\nERROR: No fue posible reconocer la opción seleccionada, vuelva a intentarlo.\n")
        return menuAdministrativo()


"""
-Nombre: menuGeneral

-Entradas: un número según la opción que desee realizar el usuario y
las demás entradas van de acuerdo a la opción seleccionada.

-Salidas: el retorno de lo realizado según las opciones escogidas entre Consulta de viajes, Reservación de viajes,
Cancelación de reservación y Salir.

-Restricciones: van según el tipo de opción escogida.
"""

    
def menuGeneral():
    print("\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨MENÚ GENERAL¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨\n")
    print("  (1) Consulta de viajes\n  (2) Reservación de viajes\n  (3) Cancelación de reservación\n  (4) Salir\n")
    print("Por favor, introduzca el número de la operación que desea realizar:")
    opcion = input("")
    opcion = int(opcion)
    if(opcion == 1):
        return 
    elif(opcion == 2):
        return
    elif(opcion == 3):
        return 
    elif(opcion == 4):
        return menuPrincipal()
    else:
        print("\nERROR: No fue posible reconocer la opcion seleccionada, vuelva a intentarlo.\n")
        return menuGeneral()



"""
Esta función muestra un menú principal del programa "Sistema de reservación de boletos" y otros sub-menús,
va hasta el final de todo el código porque sino el código se vería afectado.

-Nombre: menuPrincipal

-Entradas: un número según la opción que desee realizar el usuario y
las demás entradas van de acuerdo a la opción seleccionada.

-Salidas: el retorno de lo realizado según las opciones escogidas entre Opciones administrativas,
Opciones de usuario normal y Salir. 

-Restricciones: van según el tipo de opción escogida.
"""

def menuPrincipal():
    print("")
    print("::::::::::::::::::::::¡SISTEMA DE RESERVACIÓN DE BOLETOS!:::::::::::::::::::::\n")
    print("__________________________BIENVENID@ AL MENÚ PRINCIPAL___________________________\n")
    print("Las opciones disponibles son:\n")
    print("  (1) Opciones administrativas\n  (2) Opciones de usuario normal\n  (3) Salir\n")
    print("Por favor, introduzca el número de la operación que desea realizar: ")
    opcion = input("")
    opcion = int(opcion)
    if(opcion == 1):
        pedir_Clave_Usuario(usuario,clave)
        if(pedir_Clave_Usuario == True):
            return menuAdministrativo()
    elif(opcion == 2):
        return menuGeneral()
    elif(opcion == 3):
        return print("********¡GRACIAS POR UTILIZAR EL SISTEMA DE RESERVACIÓN DE BOLETOS!********")
    else:
        print("\nERROR: No fue posible reconocer la opcion seleccionada, vuelva a intentarlo.\n")
        return menuPrincipal()
menuPrincipal()



