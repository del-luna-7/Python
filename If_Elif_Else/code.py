# Task 1
day = int(input("Введите номер дня недели: "))

if day == 1:
    print("Понедельник")
elif day == 2:
    print("Вторник")
elif day == 3:
    print("Среда")
elif day == 4:
    print("Четверг")
elif day == 5:
    print("Пятница")
elif day == 6:
    print("Суббота")
elif day == 7:
    print("Воскресенье")
else:
    print("Неверный номер дня недели")


# Task 2
month = int(input("Введите номер месяца: "))

if month == 12 or month == 1 or month == 2:
    print("Зима")
elif month >= 3 and month <= 5:
    print("Весна")
elif month >= 6 and month <= 8:
    print("Лето")
elif month >= 9 and month <= 11:
    print("Осень")
else:
    print("Неверный номер месяца")


# Task 3
number = int(input("Введите число: "))

if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
elif number == 0:
    print("Number is equal to zero")


# Task 4
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if num1 != num2:
    if num1 < num2:
        print(num1, num2)
    else:
        print(num2, num1)
