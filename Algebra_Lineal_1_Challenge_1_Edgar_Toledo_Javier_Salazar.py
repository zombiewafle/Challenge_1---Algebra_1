#Autores: Edgar Toledo y Javier Salazar 18764
#Fecha de entrega: 17/07/19
#Descripcion: Este programa es un validador y
#calculador de digitos de control de codigos UPC,
#ISBN-10, ISBN-13, NIT y Codabar


import os
from itertools import cycle


"Verifica si es ISBN-10"
#ISBN_10 = input('Ingrese el codigo a verificar')

def digito_verificador_ISBN10(ISBN_10):
    reversed_digits = map(int, reversed(str(ISBN_10)))
    factors = [10,9,8,7,6,5,4,3,2,1]
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

#-------------------------------------------------------------------------------

"Verifica si es ISBN-13"
#ISBN_13 = input('Ingrese el codigo a verificar')

def digito_verificador_ISBN_13(ISBN_13):
    reversed_digits = map(int, reversed(str(ISBN_13)))
    factors = [1,3,1,3,1,3,1,3,1,3,1,3,1]
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 10

#-------------------------------------------------------------------------------

"Verifica si es UPC"
def digito_verificador_UPC(UPC):
    reversed_digits = map(int, reversed(str(UPC)))
    factors = [3,1,3,1,3,1,3,1,3,1,3,1]
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 10

#-------------------------------------------------------------------------------
"Verifica si es NIT"
def digito_verificador_NIT(NIT):
    reversed_digits = map(int, reversed(str(NIT)))
    factors = [10,9,8,7,6,5,4,3,2,1]
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11
#-------------------------------------------------------------------------------

"Verifica si es Codabar"
def digito_verificador_Codabar(Codabar):
    reversed_digits = map(int, reversed(str(Codabar)))
    factors = [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1]
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 10

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

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
            UPC = input("Ingrese el codigo a verificar")
            digito_verificador_UPC(UPC)
            if digito_verificador_UPC(UPC) == 0:
                print('El codigo es correcto')
            else:
                print('El codigo no es correcto')
            print("\n.....")

        elif opcionMenu2 == "2":
            print("")
            ISBN_10 = input("Ingrese el codigo a verificar")
            digito_verificador_ISBN10(ISBN_10)
            if digito_verificador_ISBN10(ISBN_10) == 0:
                print('El codigo es correcto')
            else:
                print('El codigo no es correcto')
            print("\n.....")

        elif opcionMenu2 == "3":
            print("")
            ISBN_13 = input("Ingrese el codigo a verificar")
            digito_verificador_ISBN13(ISBN_13)
            if digito_verificador_ISBN13(ISBN_13) == 0:
                print('El codigo es correcto')
            else:
                print('El codigo no es correcto')
            print("\n.....")

        elif opcionMenu2 == "4":
            print("")
            NIT = input("Ingrese el codigo a verificar")
            digito_verificador_NIT(NIT)
            if digito_verificador_NIT(NIT) == 0:
                print('El codigo es correcto')
            else:
                print('El codigo no es correcto')
            print("\n.....")

        elif opcionMenu2 == "5":
            Codabar = input("Ingrese el codigo a verificar")
            digito_verificador_Codabar(Codabar)
            if digito_verificador_Codabar(Codabar) == 0:
                print('El codigo es correcto')
            else:
                print('El codigo no es correcto')
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
