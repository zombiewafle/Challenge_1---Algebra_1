


def verify(isbn):
    isbn = input("Ingrese el isbn-10")
    counter = 1
    total = 0
    for d in reversed(isbn):
        if d is 'X':
            if counter != 1:
                return False
            d = '10'
        if d.isdigit():
            total += int(d) * counter
            counter += 1
    return counter == 11 and total % 11 == 0


def verifyISBN13(isbn13):
    isbn13 = input("Ingrese el isbn-13")
    counter = 1
    total = 0
    for d in reversed(isbn13):
        if d is 'X':
            if counter != 1:
                return False
            d = '13'
        if d.isdigit():
            total += int(d) * counter
            counter += 1
    return counter == 10 and total % 10 == 0


def verifyUPC(upc):
    upc = input("Ingrese el UPC")
    counter = 1
    total = 0
    for d in reversed(upc):
        if d is 'X':
            if counter != 1:
                return False
            d = '12'
        if d.isdigit():
            total += int(d) * counter
            counter += 1
    return counter == 10 and total % 10 == 0


def verifyNIT(nit):
    nit = input("Ingrese el NIT")
    counter = 1
    total = 0
    for d in reversed(nit):
        if d is 'X':
            if counter != 1:
                return False
            d = '13'
        if d.isdigit():
            total += int(d) * counter
            counter += 1
    return counter == 11 and total % 11 == 0

def verifyCodabar(codabar):
    codabar = input("Ingrese el Codabar")
    counter = 1
    total = 0
    for d in reversed(nit):
        if d is 'X':
            if counter != 1:
                return False
            d = '13'
        if d.isdigit():
            total += int(d) * counter
            counter += 1
    return counter == 11 and total % 11 == 0


from itertools import cycle

ISBN_13 = input('Ingrese el codigo a verificar')

def digito_verificador_ISBN_13(ISBN_13):
    reversed_digits = map(int, reversed(str(ISBN_13)))
    factors = [1,3,1,3,1,3,1,3,1,3,1,3,1]
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 10


def digito_verificador_ISBN_10(ISBN_10):
    reversed_digits = map(int, reversed(str(ISBN_10)))
    factors = [10,9,8,7,6,5,4,3,2,1]
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

def digito_verificador_UPC(UPC):
    reversed_digits = map(int, reversed(str(UPC)))
    factors = [3,1,3,1,3,1,3,1,3,1,3,1]
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 10

def digito_verificador_NIT(NIT):
    reversed_digits = map(int, reversed(str(NIT)))
    factors = [10,9,8,7,6,5,4,3,2,1]
    
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

def digito_de_control_ISBN_10(ISBN_10):
    reversed_digits = mapt(int, reversed(str(ISBN_10)))
    




print(digito_verificador_ISBN_13()(ISBN_13))

#v = [9,7,0,6,8,6,2,7,2,2]

#c = [10,9,8,7,6,5,4,3,2,1]

#vc = [a*b for a,b in zip(v,c)]

#for i in vc:
 #   i = int (i)
  #  mod = i%11
   # print (moddef





def controlDigitISBN_13   
