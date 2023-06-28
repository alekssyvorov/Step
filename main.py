def task_1():
    num_1 = int(input('Number 1 '))
    num_2 = int(input('Number 2 '))
    num_3 = int(input('Number 3 '))
    choice_user = input('Summa - 1/Multiplication - 2')
    match choice_user:
        case '1':
            return num_1 + num_2 + num_3
        case '2':
            return num_1 * num_2 * num_3


def task_2():
    num_1 = int(input('Number 1 '))
    num_2 = int(input('Number 2 '))
    num_3 = int(input('Number 3 '))
    choice_user = input('Max - 1\nMin - 2\nAverage - 3')
    match choice_user:
        case '1':
            if num_1 > num_2 and num_1 > num_3:
                return num_1
            elif num_2 > num_1 and num_2 > num_3:
                return num_2
            elif num_3 > num_1 and num_3 > num_2:
                return num_3
            else:
                return f'Number is equal'
        case '2':
            if num_1 < num_2 and num_1 < num_3:
                return num_1
            elif num_2 < num_1 and num_2 < num_3:
                return num_2
            elif num_3 < num_1 and num_3 < num_2:
                return num_3
            else:
                return f'Number is equal'
        case '3':
            return (num_1 + num_2 + num_3) / 3


def task_3():
    meters = float(input('Input meters '))
    choice_user = input('milli - 1\ninches - 2\nyards - 3')
    if choice_user == '1':
        return int(meters) * 0.000621371 + (meters - int(meters)) * 0.000621371
    elif choice_user == '2':
        return int(meters) * 25.4 + (meters - int(meters)) * 25.4
    else:
        return int(meters) * 1.09361 + (meters - int(meters)) * 1.09361


if __name__ == "__main__":
    choice = int(input('Make you choice 1/2/3 '))
    match choice:
        case 1:
            print(task_1())
        case 2:
            print(task_2())
        case 3:
            print(task_3())
