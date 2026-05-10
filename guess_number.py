from random import randint

number = randint(1,100)

while True:
    guess = int(input('Введите число: '))
    if guess > number:
        print('Меньше')
    elif guess < number:
        print('Больше')
    else:
        break
print('Вы угадали!')