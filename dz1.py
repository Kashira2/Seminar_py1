num1 = int(input('Введите цифру соответствующую дню недели от 1 до 7: '))

if num1 >= 1 and num1 <= 5:
    print('Нет')
elif num1 >= 6 and num1 <= 7:
    print('Да')
else:
    print('Введите цифру от 1 до 7')
