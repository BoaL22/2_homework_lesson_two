
    # Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
    # Найдите произведение элементов на указанных позициях. 
    # Позиции хранятся в файле file.txt в одной строке одно число.
    # (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
    # -2 -1 0 1 2
    # Позиции: 0,1 -> 2

N = int(input('Enter a number: '))
a = -N
numbers = []

with open('file.txt', 'w') as file:

    for i in range(N * 2 + 1):
        numbers.append(a)
        file.writelines(f'{a}\n')
        a += 1

with open('file.txt', 'r') as file:

    first_position = input("Еnter the first position: ") 
    second_position = input("Еnter the second position: ") 


print(numbers)
print(numbers[int(first_position)] * numbers[int(second_position)])