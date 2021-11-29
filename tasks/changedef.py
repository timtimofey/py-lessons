def change(lst):
    a = lst[0]
    b = lst[-1]

    lst[0] = b
    lst[-1] = a

mass = [5, 3, 3, 4 ,6]
change(mass)
print(mass)