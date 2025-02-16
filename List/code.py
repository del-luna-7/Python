names = ["Tamerlan", "Farid", "Radmir", "Murad", "Eldeniz", "Ramil"]
print(*names)

# Task 1
index = 0
for i in names:
    if names[index] == "Farid":
        names.insert(index, "AliMuhammad")
        names.remove("Farid")
        print(*names)
        break
    index += 1


# Task 2
name = input("Enter name: ")
exist = True
for i in names:
    if i == name:
        names.remove(name)
        print(*names)
        break
    else:
        exist = False
if not exist:
    print("Not found!")


# Task 3
index = 0
for i in names:
    if names[index] == "Eldeniz":
        names.insert(index, "Raul")
        print(*names)
        break
    index += 1


# Task 4
name = "Ramil"
revers = ""
for i in range(len(name) + 1):
    if i != 0:
        revers += name[-i]

for i in range(len(names)):
    if names[i] == "Ramil":
        names[i] = revers

print(*names)


# Task 5
symbols = 0
count = 0
for i in names:
    if i == "Tamerlan":
        for j in i:
            count += 1

print(f"Count: {count}")


# Task 6
numbers = [1, 2, 3, 4, 5]
names.append(numbers)  # Новый список для task 7
print(*names)


# Task 7
counter = 0
for i in names:
    if i == [1, 2, 3, 4, 5]:
        for j in i:
            if j == 4:
                i[counter] = "Quseyin"
            counter += 1

print(*names)

