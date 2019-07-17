#Autores: Edgar Toledo y Javier Salazar 18764
#Fecha de entrega: 17/07/19
#Descripcion: Este programa es un validador y
#calculador de digitos de control de codigos UPC,
#ISBN-10, ISBN-13, NIT y Codabar


import os


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

def validate(number):
    number = compact(number)
    if not isdigits(number):
        raise InvalidFormat()
    if len(number) not in (14, 13, 12, 8):
        raise InvalidLength()
    if calc_check_digit(number[:-1]) != number[-1]:
        raise InvalidChecksum()
    return number
"donde esta (14, 13, 12, 8) es donde va el largo del codigo"



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
