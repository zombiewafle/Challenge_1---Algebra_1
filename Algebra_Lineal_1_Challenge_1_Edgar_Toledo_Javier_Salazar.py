#Autores: Edgar Toledo y Javier Salazar 18764
#Fecha de entrega: 17/07/19
#Descripcion: Este programa es un validador y
#calculador de digitos de control de codigos UPC,
#ISBN-10, ISBN-13, NIT y Codabar


import os

"Verifica si es ISBN-10"
def verify_ISBN_10(isbn_10):
    isbn_10 = input("Ingrese el isbn-10")
    counter = 1
    total = 0
    for d in reversed(isbn_10):
        if d is 'X':
            if counter != 1:
                return False
            d = '10'
        if d.isdigit():
            total += int(d) * counter
            counter += 1
    return counter == 11 and total % 11 == 0

"Verifica si es ISBN-13"
def verify_ISBN_13(isbn_13):
    isbn_13 = input("Ingrese el isbn-13")
    counter = 1
    total = 0
    for d in reversed(isbn_13):
        if d is 'X':
            if counter != 1:
                return False
            d = '13'
        if d.isdigit():
            total += int(d) * counter
            counter += 1
    return counter == 11 and total % 11 == 0

"Verifica si es UPC"
def verify_UPC(UPC):
    UPC= input("Ingrese el UPC")
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
    return counter == 11 and total % 11 == 0

"Verifica si es NIT"
def verify_NIT(nit):
    nit = input("Ingrese el NIT")
    counter = 1
    total = 0
    for d in reversed(nit):
        if d is 'X':
            if counter != 1:
                return False
            d = '11'
        if d.isdigit():
            total += int(d) * counter
            counter += 1
    return counter == 11 and total % 11 == 0

"Verifica si es Codabar"
def verify_Codabar(codabar):
    codabar = input("Ingrese el Codabar")
    counter = 1
    total = 0
    for d in reversed(codabar):
        if d is 'X':
            if counter != 1:
                return False
            d = '13'
        if d.isdigit():
            total += int(d) * counter
            counter += 1
    return counter == 11 and total % 11 == 0




"""
Esto elimina el número de cualquier separador válido y
elimina los espacios en blanco circundantes.
"""

def compact(number):
    return clean(number, ' -').strip()

"""
Comprueba si el codigo proporcionado es válido,
esto verifica la longitud.
"""

def validateISBN_13(number):
    number = compact(number)
    if not isdigits(number):
        raise InvalidFormat()
    if len(number) not in (13):
        raise InvalidLength()
    if calc_check_digit(number[:-1]) != number[-1]:
        raise InvalidChecksum()
    return number
"donde esta (13) es donde va el largo del codigo"

def validate_ISBN_10(number):
    number = compact(number)
    if not isdigits(number):
        raise InvalidFormat()
    if len(number) not in (10):
        raise InvalidLength()
    if calc_check_digit(number[:-1]) != number[-1]:
        raise InvalidChecksum()
    return number
"donde esta (10) es donde va el largo del codigo"

def validate_NIT(number):
    number = compact(number)
    if not isdigits(number):
        raise InvalidFormat()
    if len(number) not in (10):
        raise InvalidLength()
    if calc_check_digit(number[:-1]) != number[-1]:
        raise InvalidChecksum()
    return number
"donde esta (10) es donde va el largo del codigo"

def validate_UPC(number):
    number = compact(number)
    if not isdigits(number):
        raise InvalidFormat()
    if len(number) not in (13,10):
        raise InvalidLength()
    if calc_check_digit(number[:-1]) != number[-1]:
        raise InvalidChecksum()
    return number
"donde esta (13,10) es donde va el largo del codigo"

def validate_Codabar(number):
    number = compact(number)
    if not isdigits(number):
        raise InvalidFormat()
    if len(number) not in (1,2,3,4,5,6,7,8,9,10,11,12,13,14):
        raise InvalidLength()
    if calc_check_digit(number[:-1]) != number[-1]:
        raise InvalidChecksum()
    return number
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
            verify_UPC()
            validate_UPC()
            print("\n.....")

        elif opcionMenu2 == "2":
            verify_ISBN_10()
            validate_ISBN_10()
            print("\n.....")

        elif opcionMenu2 == "3":
            verify_ISBN_13()
            validate_ISBN_13()
            print("\n.....")

        elif opcionMenu2 == "4":
            verify_NIT()
            validate_NIT()
            print("\n.....")

        elif opcionMenu2 == "5":
            verify_Codabar()
            validate_Codabar()
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
