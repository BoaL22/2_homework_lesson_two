
    # 2'. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    # пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input('Enter a number: ' ))
sum = 1
i = 1
while i <= num:
    sum = i * sum
    i += 1
    print(sum)

print(f'The product of numbers from 1 to {num} = {sum}')

