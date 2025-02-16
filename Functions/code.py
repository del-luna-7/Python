# Task 1
txt = "\"Don't let the noise of others'\nopinions drown out your own inner voice.\"\nSteve Jobs"


def text(ftxt):
    print(ftxt)


text(txt)


# Task 2
num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))


def nechetniye(fnum1, fnum2):
    while fnum1 <= fnum2:
        if fnum1 % 2 != 0:
            print(fnum1)
            fnum1 += 1
        elif fnum1 % 2 == 0:
            fnum1 += 1


nechetniye(num1, num2)


# Task 3
dlina = int(input("Dlina: "))
napravleniye = input("1-Vertikalno, 2-qorizontalno: ")
symbol = input("Simvol: ")


def liniya(fdlina, fnapravleniye, fsymbol):
    if fnapravleniye == "2":
        print(fsymbol * fdlina)
    elif fnapravleniye == "1":
        for i in range(fdlina):
            print(fsymbol)


liniya(dlina, napravleniye, symbol)


# Task 4
num1 = float(input("Num 1: "))
num2 = float(input("Num 2: "))
num3 = float(input("Num 3: "))
num4 = float(input("Num 4: "))


def maximum(fnum1, fnum2, fnum3, fnum4):
    if fnum1 > fnum2 and fnum1 > fnum3 and fnum1 > fnum4:
        return fnum1

    elif fnum2 > fnum1 and fnum2 > fnum3 and fnum2 > fnum4:
        return fnum2

    elif fnum3 > fnum1 and fnum3 > fnum2 and fnum3 > fnum4:
        return fnum3

    elif fnum4 > fnum1 and fnum4 > fnum2 and fnum4 > fnum3:
        return fnum4


print(maximum(num1, num2, num3, num4))


# Task 5
num1 = float(input("Num 1: "))
num2 = float(input("Num 2: "))
summ = 0


def summa(fnum1, fnum2, fsumm):
    while fnum1 <= fnum2:
        fsumm += fnum1
        fnum1 += 1
    return fsumm


print(summa(num1, num2, summ))


# Task 6
num = 17


def prostoye(fnum):
    count = 0
    for i in range(2, fnum):
        if fnum % i == 0:
            count += 1

    if fnum <= 2:
        return False
    else:
        if count == 0:
            return True
        else:
            return False


print(prostoye(num))


# Task 7
lst = [-1, 6, -3, 9, -4, 7, 10, 14]
cetniye = []
necetniye = []
otricatelniye = []
polojitelniye = []


def f_cetniye(flst, fcetniye):
    for i in flst:
        if i % 2 == 0:
            fcetniye.append(i)
    return fcetniye


print(f_cetniye(lst, cetniye))


def f_necetniye(flst, fnecetniye):
    for i in flst:
        if i % 2 != 0:
            fnecetniye.append(i)
    return fnecetniye


print(f_necetniye(lst, necetniye))


def f_otricatelniye(flst, fotricatelniye):
    for i in flst:
        if i < 0:
            fotricatelniye.append(i)
    return fotricatelniye


print(f_otricatelniye(lst, otricatelniye))


def f_polojitelniye(flst, fpolojitelniye):
    for i in flst:
        if i > 0:
            fpolojitelniye.append(i)
    return fpolojitelniye


print(f_polojitelniye(lst, polojitelniye))