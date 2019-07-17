


def verify(isbn):
    isbn = input("Ingrese el isbn")
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




from itertools import cycle

ISBN_13 = input('Ingrese el codigo a verificar')

def digito_verificador(ISBN_13):
    reversed_digits = map(int, reversed(str(ISBN_13)))
    factors = [1,3,1,3,1,3,1,3,1,3,1,3,1]
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 10

print(digito_verificador(ISBN_13))

#v = [9,7,0,6,8,6,2,7,2,2]

#c = [10,9,8,7,6,5,4,3,2,1]

#vc = [a*b for a,b in zip(v,c)]

#for i in vc:
 #   i = int (i)
  #  mod = i%11
   # print (mod)
