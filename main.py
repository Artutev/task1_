#ex 1

#1

print('*' * 5)


#2

height = int(input("высота треугольника: "))

for i in range(1, height + 1):
    print(' ' * (height - i) + '*' * (2 * i - 1))
