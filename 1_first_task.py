    # 1'. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

    # - 6782 -> 23
    # - 0,56 -> 11

num = input('Enter a number: ')

sum = 0
i = 0
for a in num:
    sum += int(num[int(i)])
    i += 1
print(f'Sum = {sum}')

