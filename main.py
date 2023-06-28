def task_1():
    number_day = int(input('Input number day '))
    if number_day == 1:
        return 'Monday'
    elif number_day == 2:
        return 'Tuesday'
    elif number_day == 3:
        return 'Wednesday'
    elif number_day == 4:
        return 'Thursday'
    elif number_day == 5:
        return 'Friday'
    elif number_day == 6:
        return 'Saturday '
    elif number_day == 7:
        return 'Sunday'
    else:
        return f'Error number day'


def task_2():
    num_month = int(input('Number '))
    if num_month == 12 or 1 <= num_month <= 2:
        return 'Winter'
    elif 3 <= num_month <= 5:
        return 'Spring'
    elif 3 <= num_month <= 5:
        return 'Summer'
    elif num_month >= 6 and num_month <= 11:
        return 'Autumn'
    else:
        return 'Error input'


def task_3():
    num = int(input('Number '))
    if num > 0:
        return 'Number is positive'
    elif num < 0:
        return 'Number is negative'
    else:
        return 'Number is equal to zero'


def task_4():
    num_1 = int(input('Number 1'))
    num_2 = int(input('Number 2'))
    if num_1 == num_2:
        return 'The numbers are equal'
    else:
        if num_1 > num_2:
            return num_1, num_2
        else:
            return num_2, num_1


if __name__ == "__main__":
    choice = int(input('Make you choice 1/2/3/4 '))
    match choice:
        case 1:
            print(task_1())
        case 2:
            print(task_2())
        case 3:
            print(task_3())
        case 4:
            print(task_4())
