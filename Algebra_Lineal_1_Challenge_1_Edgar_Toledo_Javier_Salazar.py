#Autores: Edgar Toledo y Javier Salazar 18764
#Fecha de entrega: 17/07/19
#Descripcion: Este programa es un validador y
#calculador de digitos de control de codigos UPC,
#ISBN-10, ISBN-13, NIT y Codabar


import os
#isbn_10 = input("Ingrese el isbn-10")
#isbn_13 = input("Ingrese el isbn-13")
#UPC= input("Ingrese el UPC")
#nit = input("Ingrese el NIT")
#codabar = input("Ingrese el Codabar")

"Verifica si es ISBN-10"
def verify_ISBN_10(ISBN_10):
    counter = 1
    total = 0
    for d in reversed(ISBN_10):
        if d is 'X':
            if counter != 1:
                return False
            d = '10'
        if d.isdigit():
            total += int(d) * counter
            counter += 1
    return counter == 11 and total % 11 == 0

"Verifica si es ISBN-13"
def verify_ISBN_13(ISBN_13):
    counter = 1
    total = 0
    for d in reversed(ISBN_13):
        if d is 'X':
            if counter != 1:
                return False
            d = '13'
        if d.isdigit():
            total += int(d) * counter
            counter += 1
    return counter == 13 and total % 13 == 0

"Verifica si es UPC"
def verify_UPC(UPC):
    counter = 1
    total = 0
    for d in reversed(UPC):
        if d is 'X':
            if counter != 1:
                return False
            d = '10'
        if d.isdigit():
            total += int(d) * counter
            counter += 1
    return counter == 10 and total % 10 == 0

"Verifica si es NIT"
def verify_NIT(NIT):
    counter = 1
    total = 0
    for d in reversed(NIT):
        if d is 'X':
            if counter != 1:
                return False
            d = '11'
        if d.isdigit():
            total += int(d) * counter
            counter += 1
    return counter == 10 and total % 10 == 0

"Verifica si es Codabar"
def verify_Codabar(Codabar):
    counter = 1
    total = 0
    for d in reversed(Codabar):
        if d is 'X':
            if counter != 1:
                return False
            d = '13'
        if d.isdigit():
            total += int(d) * counter
            counter += 1
    return counter == 16 and total % 16 == 0

#-------------------------------------------------------------------------------


"""
Esto elimina el número de cualquier separador válido y
elimina los espacios en blanco circundantes.
"""

def compact_13(ISBN_13):
    return clean(ISBN_13, ' -').strip()

def compact_10(ISBN_10):
    return clean(ISBN_10, ' -').strip()

def compact_NIT(NIT):
    return clean(NIT, ' -').strip()

def compact_UPC(UPC):
    return clean(UPC, ' -').strip()

def compact_Codabar(Codabar):
    return clean(Codabar, ' -').strip()
#-------------------------------------------------------------------------
"""
Comprueba si el codigo proporcionado es válido,
esto verifica la longitud.
"""

def validateISBN_13(ISBN_13):
    ISBN_13 = compact_13(ISBN_13)
    if not isdigits(ISBN_13):
        raise InvalidFormat()
    if len(ISBN_13) not in (13):
        raise InvalidLength()
    if calc_check_digit(ISBN_13[:-1]) != ISBN_13[-1]:
        raise InvalidChecksum()
    return ISBN_13
"donde esta (13) es donde va el largo del codigo"

def validate_ISBN_10(ISBN_10):
    ISBN_10 = compact_10(ISBN_10)
    if not isdigits(ISBN_10):
        raise InvalidFormat()
    if len(ISBN_10) not in (10):
        raise InvalidLength()
    if calc_check_digit(ISBN_10[:-1]) != ISBN_10[-1]:
        raise InvalidChecksum()
    return ISBN_10
"donde esta (10) es donde va el largo del codigo"

def validate_NIT(number):
    number = compact_NIT(number)
    if not isdigits(number):
        raise InvalidFormat()
    if len(number) not in (10):
        raise InvalidLength()
    if calc_check_digit(number[:-1]) != number[-1]:
        raise InvalidChecksum()
    return number
"donde esta (10) es donde va el largo del codigo"

def validate_UPC(UPC):
    UPC = compact_UPC(UPC)
    if not isdigits(UPC):
        raise InvalidFormat()
    if len(UPC) not in (13,10):
        raise InvalidLength()
    if calc_check_digit(UPC[:-1]) != UPC[-1]:
        raise InvalidChecksum()
    return UPC
"donde esta (13,10) es donde va el largo del codigo"

def compact_Codabar(Codabar):
    Codabar = compact(Codabar)
    if not isdigits(Codabar):
        raise InvalidFormat()
    if len(Codabar) not in (1,2,3,4,5,6,7,8,9,10,11,12,13,14):
        raise InvalidLength()
    if calc_check_digit(Codabar[:-1]) != Codabar[-1]:
        raise InvalidChecksum()
    return Codabar
"donde esta (1,2,3,4,5,6,7,8,9,10,11,12,13,14) es donde va el largo del codigo"

#-----------------------------------------------------------------

def menu2():
    print("""
            Elija el código que desea utilizar:\n
            Menu:\n
            1. UPC.\n
            2. ISBN-10.\n
            3. ISBN-13.\n
            4. NIT.\n
            5. Codabar.\n
            6. Regresar al primer menu.\n
          """
          )

def menu1():
    print("""
            Elija la acción que desea realizar:\n
            Menu:\n
            1. Calcular un código.\n
            2. Calcular un digito de control.\n
            3. Terminar el programa.\n
            """
          )

   
while True:
    menu1()

    opcionMenu = input("Inserte un valor >>")
    if opcionMenu == "1":
        print("")
        menu2()
        opcionMenu2 = input("Inserte un valor >>")
        if opcionMenu2 == "1":
            print("")
            UPC = input("Ingrese el codigo a verificar y validar")
            verify_UPC(UPC)
            validate_UPC(UPC)
            print("\n.....")

        elif opcionMenu2 == "2":
            verify_ISBN_10(ISBN_10)
            validate_ISBN_10(ISBN_10)
            print("\n.....")

        elif opcionMenu2 == "3":
            verify_ISBN_13(ISBN_13)
            validate_ISBN_13(ISBN_13)
            print("\n.....")

        elif opcionMenu2 == "4":
            verify_NIT(NIT)
            validate_NIT(NIT)
            print("\n.....")

        elif opcionMenu2 == "5":
            verify_Codabar(Codabar)
            validate_Codabar(Codabar)
            print("\n.....")

        elif opcionMenu2 == "6":
            print("OK, saliendo en...")
            print("..3..2..1")
            menu1()
            
        input("Has pulsado la opcion 1....\npulsa una tecla para continuar")

    elif opcionMenu =="2":
        print("")
        menu2()
        input("Has pulsado la opcion 2....\npulsa una tecla para continuar")

    elif opcionMenu =="3":
        print("....")
        print("Adios... Vuelva pronto!!!!")
        break

    else:
        print()
        input("No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")
