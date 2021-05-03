#..................................Proyecto-Sistema de reservación de viajes..........................................#
                                            #Taller de Programación#
#Angélica Díaz Barrios
#2021044256

#===================================CREAR, REGISTRAR Y OBTENER USUARIO-CLAVE==========================================#

"""
Nombre: obtener_Usuario
Entrada: el nombre del archivo "usuariosClaves.txt"
Salida: el recorrido de todo el archivo ("usuariosClaves.txt") línea por línea
Restricciones: se debe llamar al archivo correcto para que se puedan recorrer las líneas
"""
def obtener_Usuario():
    datos = open("usuariosClaves.txt")
    info = datos.readlines()
    datos.close()
    return info

"""
Nombre: registrar_usuario_clave
Entrada: la clave y el nombre del usuario
Salida:el retorno a la función anotarDatosUsuario.
Restricciones: no existen
"""
def registrar_usuario_clave():
    print("\n-----------------Creando Usuario------------------------\n")
    clave = input("Ingrese una clave-contraseña: ")
    nombre = input("Ingrese el nombre de usuario: ")
    return anotarDatosUsuario(clave, nombre)

"""
Nombre: buscarClave
Entrada: (linea, clave), la linea en donde se ubica la clave y la clave del usuario
Salida: El retorno de True si la clave fue encontrada en la linea o False si no la encontró.
Restricciones: la clave siempre se localizará en la posición cero
"""
def buscarClave(linea, clave):
    claveEncontrada = linea.split(",")[0]
    palabra = clave
    for letra in palabra:
        if(letra == "\""):
            return palabra
    if(claveEncontrada == clave):
        return True
    else:
        return False

"""
Nombre: validarUsuario
Entrada: (clave), la clave del usuario
Salida: El retorno de True si la clave ya existe en el archivo o False si no existe dentro del archivo
"usuariosClaves.txt"
Restricciones: se debe abrir al archivo en modo lectura
"""
def validarUsuario(clave):
    archivo = ("usuariosClaves.txt")
    datos = open(archivo, "r")
    lineas = datos.readlines()
    for linea in lineas:
        claveExiste = buscarClave(linea, clave)
    if(claveExiste == True):
        return True
    else:
        return False
    
"""
Nombre: anotarDatosUsuario
Entradas: (clave, nombre) recibe la clave primero y luego el nombre del usuario
Salida: el retorno a la función pedir_Clave_Usuario()
Restricciones: se debe abrir el archivo correcto con "a" para que se pueda agregar el usuario.
"""
def anotarDatosUsuario(clave, nombre):
    datos = open("usuariosClaves.txt", "a")
    datos.write(clave + ", " + nombre + "\n")
    print("\nSu usuario fue agregado exitosamente\n\nYa puede ingresar al menú administrativo utilizando solo su clave")
    datos.close()
    return pedir_Clave_Usuario()
    
    
    
"""
Nombre: pedir_Clave_Usuario
Entradas: la clave del usuario para poder registrarse
Salidas: el retorno al menú administrativo si la contraseña se encontraba resgistrada en el archivo
o el retorno a la función registrar_usuario_clave() si no se encontró la clave en el archivo
"""
def pedir_Clave_Usuario():
    print("--------------------------------------------------------------------------------")
    print("\nRegistrese con la clave de su usuario para poder accerder al menú administrativo\n")
    clave = input("Ingrese la clave: ")
    if(validarUsuario(clave) == True):
        return menuAdministrativo()
    else:
        print("\nLa clave no se encuentra registrada, por favor cree un usuario\n")
        return registrar_usuario_clave()
    
#=============================================GESTIÓN DE EMPRESAS===================================================#    

"""
Nombre: gestion_Empresas
Entrada: un número entero
Salida: el retorno a la opción escogida de acuerdo al número ingresado en la entrada,
entre las opciones están: Incluir empresa, Eliminar empresa, Modificar empresa, Mostrar Empresas, Salir
Restricciones: se debe ingresar un número entero para acceder a las funciones de las opciones y el resto
de restricciones van de acuerdo a cada opción.
"""

def gestion_Empresas():
    print("\n-----------------------------GESTIÓN DE EMPRESAS-----------------------------------\n")
    print("\n  (1) Incluir empresa\n  (2) Eliminar empresa\n  (3) Modificar empresa\n  (4) Mostrar Empresas\n  (5) Salir\n")
    print("Por favor, introduzca el número de la operación que desea realizar: ")
    opcion = input("")
    opcion = int(opcion)
    if(opcion == 1):
        return incluirEmpresa()
    elif(opcion == 2):
        print("-------------------------------Eliminando empresa------------------------------")
        cedula = input("\ningrese la cédula jurídica de la empresa que desea eliminar: ")
        return eliminarEmpresa(cedula)
    elif(opcion == 3):
        print("-------------------------------modificando empresa------------------------------")
        cedula = input("\ningrese la cédula jurídica de la empresa que desea modificar: ")
        return modificarEmpresa(cedula)
    elif(opcion == 4):
        print("-------------------------------Mostrando empresas------------------------------")
        print("\nLas empresas registradas actualmente son:\n")
        return verEmpresas()
    elif(opcion == 5):
        return menuAdministrativo()
    else:
        print("\nERROR: No fue posible reconocer la opción seleccionada, vuelva a intentarlo.\n")
        return menuAdministrativo()
        

"""
Nombre: incluirEmpresa
Entrada: la cédula jurídica, el nombre de la empresa y la ubicación de la empresa
Salida: el retorno a la función anotarDatosEmpresa, para que la empresa pueda ser agregada
Restricciones: la cédula jurídica debe tener 10 dígitos.
"""
def incluirEmpresa():
    print("\n-----------------Incluyendo empresa------------------------\n")
    cedula = input("Ingrese la cédula jurídica de la empresa: ")
    if(largoTexto(cedula) == 10):
        empresa = input("Ingrese el nombre de la empresa: ")
        ubicacion = input("Ingrese la dirreción-ubicación de la empresa: ")
        return anotarDatosEmpresa(cedula, empresa, ubicacion)
    else:
        print("\nError: la cédula jurídica debe contener 10 dígitos, por lo tanto la empresa no se podrá incluir")
        return gestion_Empresas()
    

"""
Nombre: largoTexto
Entradas: texto: una palabra o texto 
Salidas: un número entero  que representa la cantidad de letras que contiene el string
Restricciones: se debe ingresar el tipo de dato string, ningún otro se permite.
"""    
def largoTexto(texto):
     if(isinstance(texto,str) and (texto != "")):
          return largoTexto_aux(texto, 0)
     else:
          return 0

def largoTexto_aux(texto, resultado):
     if(texto == ""):
          return resultado
     else:
          return largoTexto_aux(texto[1:], resultado +1)
           
"""
Nombre: anotarDatosEmpresa
Entradas: la cédula jurídica, el nombre de la empresa y la ubicación de la empresa
Salidas: la impresión de que el usuario fue agregado al archivo "Empresas.txt"
Restricciones: se debe abrir el archivo "Empresas.txt" con "a" para la empresa se pueda agregar exitosamente,
además no se registrará la empresa si la cédula jurídica se repite con una ya existente dentro del archivo "Empresas.txt"
"""

def anotarDatosEmpresa(cedula, empresa, ubicacion):
    archivoo = ("Empresas.txt")
    datosl = open(archivoo, "r")
    lineas = datosl.readlines()
    datosl.close()
    for linea in lineas:
        cedulaExiste = buscarCedula(linea, cedula)
    linea = ","
    cedulaExiste = buscarCedula(linea, cedula)
    if(cedulaExiste == False):
        datos = open("Empresas.txt", "a")
        datos.write(cedula + "," + empresa + "," + ubicacion + "\n")
        datos.close()
        print("\nLa empresa fue agregada exitosamente\n")
        return gestion_Empresas()
    else:
        print("\nError: la cédula jurídica de la empresa ya se encuentra registrada, intente con una cédula diferente")
        return gestion_Empresas()
    
    
"""
Nombre: verEmpresas
Entrada: el nombre del archivo en el cual se encuentran las empresas.
Salida: el print de todas las empresas ingresadas en total
Restricciones: se debe abrir el archivo en modo lectura
"""
def verEmpresas():
    archivo = ("Empresas.txt")
    f = open (archivo,'r')
    for mensaje in f.readlines():
        print(mensaje)
    f.close()
    return gestion_Empresas()

"""
Nombre: eliminarEmpresas
Entradas: la cédula jurídica de la empresa
Salida: si la cédula se encuentra dentro del archivo Empresa.txt, la empresa se eliminará y si no se encuentra,
se imprimirá un mensaje de error y se devolverá a la función gestion_Empresas.
Restricciones: se debe ingresar la cédula correcta para poder borrar la empresa
"""

def eliminarEmpresa(cedula):
    archivo = "Empresas.txt"
    seBorro = False 
    datosViejos = open(archivo, "r")
    lineas = datosViejos.readlines()
    datosViejos.close()
    datosNuevos = open(archivo, "w")
    for linea in lineas:
        cedulaExiste = buscarCedula(linea, cedula)
        if(cedulaExiste == True):
            seBorro = True
        else:
            datosNuevos.write(linea)
    datosNuevos.close()
    if(seBorro == True):
        print("\nLa empresa ha sido eliminada exitosamente\n")
        return gestion_Empresas()
    else:
        print("\nERROR: La empresa con ese número de cédula no fue posible encontrarla")
        return gestion_Empresas()


"""
Nombre: modificarEmpresa
Entradas: la cédula jurídica de la empresa
Salida: si la cédula se encuentra dentro del archivo Empresa.txt, la empresa se modificará y si no se encuentra,
se imprimirá un mensaje de error y se devolverá a la función gestion_Empresas.
Restricciones: se debe ingresar la cédula correcta para poder modificar la empresa.
"""
def modificarEmpresa(cedula):
    archivo = "Empresas.txt"
    seBorro = False 
    datosViejos = open(archivo, "r")
    lineas = datosViejos.readlines()
    datosViejos.close()
    datosNuevos = open(archivo, "w")
    for linea in lineas:
        cedulaExiste = buscarCedula(linea, cedula)
        if(cedulaExiste == True):
            seBorro = True 
        else:
            datosNuevos.write(linea)
    datosNuevos.close()
    if(seBorro == True):
        print("\nACONTINUACIÓN: Escriba las modificaciones a la empresa.\n")
        print("Debe volver a reescribir lo que quiere conservar y cambiar lo que desea modificar\n")
        return incluirEmpresa()
        gestion_Empresas()
    else:
        print("\nERROR: no se encontró el número de cédula, por lo tanto, no podrá modificar ninguna empresa\n")
        
        return gestion_Empresas()

"""
Nombre: buscarCedula
Entrada: (linea, cedula), la linea en donde se ubica la cedula y la cédula jurídica de la empresa
Salida: El retorno de True si la cédula fue encontrada en la linea o False si no la encontró.
Restricciones: la cédula siempre se localizará en la posición cero
"""
def buscarCedula(linea, cedula):
    cedulaEncontrada = linea.split(",")[0]
    palabra = cedula
    for letra in palabra:
        if(letra == "\""):
            return palabra
    if(cedulaEncontrada == cedula):
        return True
    else:
        return False
"""
Nombre: validarEmpresa
Entrada: (cédula), la cédula jurídica de la empresa 
Salida: El retorno de True si la cédula ya existe en el archivo o False si no existe dentro del archivo"Empresas.txt"
Restricciones: se debe abrir al archivo en modo lectura
"""
def validarEmpresa(cedula):
    archivo = ("Empresas.txt")
    datos = open(archivo, "r")
    lineas = datos.readlines()
    datos.close()
    for linea in lineas:
        cedulaExiste = buscarCedula(linea, cedula)
        if(cedulaExiste == True):
            return True
        else:
            return False

#======================================GESTIÓN DE TRANSPORTE POR EMPRESA============================================#

"""
Nombre: gestion_Transporte_Empresa
Entrada: un número entero
Salida: el retorno a la opción escogida de acuerdo al número ingresado en la entrada,
entre las opciones están: Incluir transporte, Eliminar transporte, Modificar transporte, Mostrar Transporte, Salir
Restricciones: se debe ingresar un número entero solo los que aparecen en las opciones para acceder a las funciones
de las opciones y el resto de restricciones van de acuerdo a cada opción.
"""

def gestion_Transporte_Empresa():
    print("\n----------------------GESTIÓN DE TRANSPORTE POR EMPRESA----------------------------\n")
    print("\n  (1) Incluir transporte\n  (2) Eliminar transporte\n  (3) Modificar transporte\n  (4) Mostrar transportes\n  (5) Salir\n")
    print("Por favor, introduzca el número de la operación que desea realizar: ")
    opcion = input("")
    opcion = int(opcion)
    if(opcion == 1):
        return incluirTransporte()
    elif(opcion == 2):
        print("-------------------------------Eliminando transporte------------------------------")
        placa = input("\ningrese el número de placa del transporte que desea eliminar: ")
        return eliminarTransporte(placa)
    elif(opcion == 3):
        print("-------------------------------Modificando transporte------------------------------")
        placa = input("\ningrese el número de placa del transporte que desea modificar: ")
        return modificarTransporte(placa)
    elif(opcion == 4):
        print("-------------------------------Mostrando transportes------------------------------")
        print("\nLos transportes registrados actualmente son:\n")
        return verTransportes()
    elif(opcion == 5):
        return menuAdministrativo()
    else:
        print("\nERROR: No fue posible reconocer la opción seleccionada, vuelva a intentarlo.\n")
        return menuAdministrativo()

"""
Nombre: incluirTransporte
Entrada: la  placa del transporte, la marca del transporte, Modelo, año, empresa a la que pertenece el transporte y la
cantidad de asientos vip, clase normal y clase económica.
Salida: el retorno a la función anotarDatosTransporte, para que el transporte pueda ser agregado
Restricciones: el año debe tener 4 dígitos exactos
"""
def incluirTransporte():
    print("\n-----------------Incluyendo Transporte------------------------\n")
    placa = input("Ingrese la placa del transporte: ")
    marca = input("Ingrese la marca del transporte: ")
    modelo = input("Ingrese el modelo del transporte: ")
    año = int(input("Ingrese el año del transporte: "))
    if(largo(año) == 4):
        empresa = input("Ingrese el nombre de la empresa a la que desea asociar el transporte,\npuede asociar el transporte a una empresa ya registrada en la base de datos:\n")
        print("Ingrese la cantidad de asientos según la categoría:")
        clasevip = int(input("clase vip: "))
        clasenormal = int(input("clase normal: "))
        claseEconomica = int(input("clase económica: "))
        return anotarDatosTransporte(placa, marca, modelo, año, empresa, clasevip, clasenormal, claseEconomica)
    else:
        print("El año ingresado no es válido, debe poseer 4 dígitos exactos")
        return incluirTransporte()

"""
Nombre: largo
Entrada: un número mayor o igual a cero
Salidad: cantidad de dígitos que posee el numero ingresado.
Restrincción: el número debe de ser entero positivo
"""

def largo(num):
    if(isinstance(num, int) == False):
        return print("Error tipo de dato, no es entero")
    elif (num == 0):
         return 1
    else:
        return largo_aux(num, 0)

def largo_aux(n, resultado):
    if(n == 0):
        return resultado
    else:
        return  largo_aux(n // 10, resultado +1)
    
"""
Nombre: anotarDatosTransporte
Entradas: la  placa del transporte, la marca del transporte, Modelo, año, empresa a la que pertenece el transporte y la
cantidad de asientos vip, clase normal y clase económica.
Salidas: el print de que el transporte fue agregado al archivo "Empresa.txt" o el retorno a la función
gestion_Transporte_Empresa si no se pudo agregar.
Restricciones: se debe abrir el archivo "Transportes.txt" con "a" para que el transporte se pueda agregar exitosamente,
además se no se puede agregar si la matrícula-placa ya se encuentra resgistrada dentro del archivo "Transportes.txt" .
"""

def anotarDatosTransporte(placa, marca, modelo, año, empresa, clasevip, clasenormal, claseEconomica):
    archivol = ("Transportes.txt")
    datosl = open(archivol, "r")
    lineas = datosl.readlines()
    datosl.close()
    for linea in lineas:
        placaExiste = buscarPlaca(linea, placa)
    linea = ","
    placaExiste = buscarPlaca(linea, placa)
    if(placaExiste == False):
        datos = open("Transportes.txt", "a")
        datos.write(placa + "," + marca + "," + modelo + "," + str(año) + "," + empresa + "," + str(clasevip) + "," + str(clasenormal) + "," + str(claseEconomica) + "\n")
        print("\nEl transporte fue registrado exitosamente\n")
        datos.close()
        return gestion_Transporte_Empresa()
    else:
        print("\nError: el transporte con la matrícula de esa placa ya existe, por lo tanto; el transporte no se podrá resgistrar")
        return gestion_Transporte_Empresa()


"""
Nombre: verTransportes
Entrada: el nombre del archivo en el cual se encuentran los transportes.
Salida: el print de todos los transportes ingresados en total
Restricciones: se debe abrir el archivo en modo lectura
"""

def verTransportes():
    archivo = ("Transportes.txt")
    f = open (archivo,'r')
    for mensaje in f.readlines():
        print(mensaje)
    f.close()
    return gestion_Transporte_Empresa()

"""
Nombre: eliminarTransporte
Entradas: la placa del trasnporte que se desea eliminar
Salida: si la placa se encuentra dentro del archivo Transportes.txt, el transporte se eliminará y si no se encuentra,
se imprimirá un mensaje de error y se devolverá a la función gestion_Transporte_Empresas.
Restricciones: se debe ingresar la placa correcta para poder borrar el transporte
"""

def eliminarTransporte(placa):
    archivo = "Transportes.txt"
    seBorro = False 
    datosViejos = open(archivo, "r")
    lineas = datosViejos.readlines()
    datosViejos.close()
    datosNuevos = open(archivo, "w")
    for linea in lineas:
        placaExiste = buscarPlaca(linea, placa)
        if(placaExiste == True):
            seBorro = True
        else:
            datosNuevos.write(linea)
    datosNuevos.close()
    if(seBorro == True):
        print("\nEl transporte ha sido eliminado exitosamente\n")
        return gestion_Transporte_Empresa()
    else:
        print("\nERROR: El transporte con esa placa no fue posible encontrarlo")
        return gestion_Transporte_Empresa()


"""
Nombre: modificarTransporte
Entradas: la placa del transporte a modificar
Salida: si la placa se encuentra dentro del archivo Transportes.txt, el transporte se modificará y si no se encuentra,
se imprimirá un mensaje de error y se devolverá a la función gestion_Empresas.
Restricciones: se debe ingresar la placa correcta para poder modificar el transporte
"""
def modificarTransporte(placa):
    archivo = "Transportes.txt"
    seBorro = False 
    datosViejos = open(archivo, "r")
    lineas = datosViejos.readlines()
    datosViejos.close()
    datosNuevos = open(archivo, "w")
    for linea in lineas:
        placaExiste = buscarPlaca(linea, placa)
        if(placaExiste == True):
            seBorro = True 
        else:
            datosNuevos.write(linea)
    datosNuevos.close()
    if(seBorro == True):
        print("\nACONTINUACIÓN: Escriba las modificaciones al transporte.\n")
        print("Debe volver a reescribir lo que quiere conservar y cambiar lo que desea modificar\n")
        return incluirEmpresa()
        gestion_Transporte_Empresa()
    else:
        print("\nERROR: no se encontró el número de placa, por lo tanto, no podrá modificar ningún transporte\n")
        
        return gestion_Transporte_Empresa()

"""
Nombre: buscarPlaca
Entrada: (linea, placa), la linea en donde se ubica la placa y la placa del transporte
Salida: El retorno de True si la placa fue encontrada en la linea o False si no la encontró.
Restricciones: la placa siempre se localizará en la posición cero
"""
def buscarPlaca(linea, placa):
    placaEncontrada = linea.split(",")[0]
    palabra = placa
    for letra in palabra:
        if(letra == "\""):
            return palabra
    if(placaEncontrada == placa):
        return True
    else:
        return False
"""
Nombre: validarTransporte
Entrada: (placa), la placa del transporte 
Salida: El retorno de True si la placa ya existe en el archivo o False si no existe dentro del archivo"Transportes.txt"
Restricciones: se debe abrir al archivo en modo lectura
"""
def validarTransporte(placa):
    archivo = ("Transportes.txt")
    datos = open(archivo, "r")
    lineas = datos.readlines()
    datos.close()
    for linea in lineas:
        placaExiste = buscarPlaca(linea, placa)
        if(placaExiste == True):
            return True
        else:
            return False







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
    print("\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨MENÚ ADMINISTRATIVO¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨\n")
    print("  (1) Gestión de empresas\n  (2) Gestión de transporte por empresa\n  (3) Gestión de viajes")
    print("  (4) Consultar historial de reservaciones\n  (5) Volver al menú principal\n")
    print("Por favor, introduzca el número de la operación que desea realizar: ")
    opcion = input("")
    opcion = int(opcion)
    if(opcion == 1):
        return gestion_Empresas()
    elif(opcion == 2):
        return gestion_Transporte_Empresa()
    elif(opcion == 3):
        return gestion_Viajes()
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
    print("  (1) Consulta de viajes\n  (2) Reservación de viajes\n  (3) Cancelación de reservación\n  (4) Volver al menú principal\n")
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
        return pedir_Clave_Usuario()
    elif(opcion == 2):
        return menuGeneral()
    elif(opcion == 3):
        return print("********¡GRACIAS POR UTILIZAR EL SISTEMA DE RESERVACIÓN DE BOLETOS!********")
    else:
        print("\nERROR: No fue posible reconocer la opcion seleccionada, vuelva a intentarlo.\n")
        return menuPrincipal()
menuPrincipal()




