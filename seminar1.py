# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите первое число: '))

# #### if num1 == num2**2 or num2 == num1**2

# if num1 == num2**2:
#     print('да')    
# elif num2 == num1**2: 
#     print(f'{num2} является квадратом {num1}')
# else :
#     print('нет')
############################################################3

array = []
for i in range(5):   
    array.append(int(input("Введите элемент списка: ")))
# range(0, 10, 2)  0 - от какого числа, 10 - до девяти, 2 - шаг (0, 2, 4, 6, 8)

print(array)
#print(max(array))

my_max = array[0]

for item in array:
    if my_max < item:
        my_max = item

print(my_max)
        
# если ищем индекс, а не сам элемент то пишем
# for i in range(len(array)):
# print(i)
