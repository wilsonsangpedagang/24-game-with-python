from math import *
from random import *
from random import randrange

print('Game 24 broo ')
a = randrange(1,11)
b = randrange(1,11)
c = randrange(1,11)
d = randrange(1,11)

list = [a,b,c,d]
print(list)

operator = None

def numbers(x):
    while x not in list:
        x = int(input("Angka: "))
    return x


def operator(x, y):
    ulangoperator = True
    while ulangoperator == True:
        operator = str(input('Harus diapain biar jadi 24 ? '))
        if operator == "+":
            hasil1 = x + y
            ulangoperator = False
        elif operator == "-":
            hasil1 = x - y
            ulangoperator = False
        elif operator == "/":
            hasil1 = x / y
            ulangoperator = False
        elif operator == "*":
            hasil1 = x * y
            ulangoperator = False
        elif operator == "**":
            hasil1 = x ** y
            ulangoperator = False
        else:
            print("Coba lihat lagi operatornya ! ")

        
    hasil1 = int(hasil1)
    return [hasil1, operator]
    
    

while True:
    angka1 = None
    angka2 = None

    i1 = numbers(angka1)
    i2 = numbers(angka2)
    op1 = operator(i1, i2)
    list.append(op1[0])
    list.remove(i1)
    list.remove(i2)
    operator = op1[1]

    str(print(i1, operator, i2, "=", op1[0]))
    print(list)

    angka3 = None
    angka4 = None
    i3 = numbers(angka3)
    i4 = numbers(angka4)
    op2 = operator(i3, i4)
    list.append(op2[0])
    list.remove(i4)
    list.remove(i3)
    operator = op2[1]

    str(print(i3, operator, i4, "=", op2[0]))
    print(list)

    angka5 = None
    angka6 = None
    i5 = numbers(angka5)
    i6 = numbers(angka6)
    op3 = operator(i5, i6)
    list.append(op3[1])
    list.remove(i6)
    list.remove(i5)
    operator = op3[1]

    str(print(i5, operator, i6, "=", op3[0]))
    print(list)

    if op3 == 24:
        print("you win !")
    else:   
        print("wrong ! ")

    playAgain = None
    while playAgain not in ["Y", "N"]:
        playAgain = input("play again? Y/N ")
        playAgain = playAgain.upper()
    if playAgain != "Y":
        break



