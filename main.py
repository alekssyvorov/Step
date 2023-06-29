def task_1(number: int):
    if number % 2 == 0:
        print(number, 'Even number.')
    else:
        print(number, 'Odd number.')


def task_2(number: int):
    if number % 7 == 0:
        print('Number is a multiple of 7.')
    else:
        print('Number is not a multiple of 7.')


def task_3(number1: float, number2: float):
    if number1 > number2:
        print(number1)
    else:
        print(number2)


def task_4(number1: float, number2: float):
    if number1 < number2:
        print(number1)
    else:
        print(number2)


def task_5(number1: float, number2: float, sign: str):
    if sign == '+':
        print(number1 + number2)
    elif sign == '-':
        print(number1 - number2)
    elif sign == 'average':
        print(2 / (number1 + number2))
    elif sign == '*':
        print(number1 * number2)


if __name__ == "__main__":
    choice = int(input('Make you choice 1/2/3/4/5 '))
    match choice:
        case 1:
            number = int(input('Enter the number: '))
            task_1(number)
        case 2:
            number = int(input('Enter the number: '))
            task_2(number)
        case 3:
            number1 = float(input('Enter the first number: '))
            number2 = float(input('Enter the second number: '))
            task_3(number1, number2)
        case 4:
            number1 = float(input('Enter the first number: '))
            number2 = float(input('Enter the second number: '))
            task_4(number1, number2)
        case 5:
            number1 = int(input('Enter the first number: '))
            number2 = int(input('Enter the second number: '))
            sign = input('Enter the sign: +-average')
            task_5(number1, number2, sign)
