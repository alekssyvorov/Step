import math


def task_1(time_second: int, choice: str) -> int:
    match choice.lower():
        case 'h':
            return int(24 - time_second / 3600)
        case 'm':
            return int(1440 - time_second / 360)
        case 's':
            return 86400 - time_second


def task_2(diam: float, choice_user: str) -> float:
    match choice_user.lower():
        case 's':
            return math.pi * math.sqrt(diam / 2)
        case 'p':
            return math.pi * diam


def task_3(price: float, count: int, discount: int, choice_user: str) -> float:
    match choice_user.lower():
        case '1':
            return price - price * discount / 100
        case 'all':
            return count * (price - price * discount / 100)


def task_4(size: float, speed: int, choice: str) -> int:
    match choice.lower():
        case 'h':  # 2  100 200/c
            return int(size * 8e+9 / speed / 360)
        case 'm':
            return int(size * 8e+9 / speed / 60)
        case 's':
            return int(size * 8e+9 / speed)


def task_5(t_d: int) -> str:
    if 0 < t_d < 6:
        return f'Good Night'
    elif 6 <= t_d < 13:
        return f'Good Morning'
    elif 13 <= t_d < 17:
        return f'Good Day'
    elif 17 <= t_d <= 24 or t_d == 0:
        return 'Good Evening'


if __name__ == "__main__":
    choice = int(input('Make you choice 1/2/3/4/5 '))
    match choice:
        case 1:
            time_second = int(input('Enter the second: '))
            choice = input('Input h/m/s ')
            print(task_1(time_second, choice))
        case 2:
            d = float(input('Enter the diameter: '))
            choice = input('Input s/p ')
            print(task_2(d, choice))
        case 3:
            price = float(input('Enter the price : '))
            count = int(input('Enter the quantity: '))
            discount = int(input('Enter the discount: '))
            choice = input('Make your choice 1/all')
            print(task_3(price, count, discount, choice))
        case 4:
            size = float(input('Enter the size file: '))
            speed = int(input('Enter the speed: '))
            choice = input('Make your choice h/m/s: ')
            print(task_4(size, speed, choice))
        case 5:
            time_day = int(input('Enter the time of day: '))
            print(task_5(time_day))
