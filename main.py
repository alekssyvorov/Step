def task_1():
    num_1 = int(input('Number 1 '))
    num_2 = int(input('Number 2 '))
    return num_1 + num_2, num_1 - num_2, num_1 * num_2


def task_2():
    number = int(input('Input number '))
    percent = int(input('Input percent '))
    return int(number * percent / 100)


def task_3():
    height = float(input('Input height '))
    width = float(input('Input width '))
    return height * width


if __name__ == "__main__":
    choice = int(input('Make you choice 1/2/3/4/5'))
    match choice:
        case 1:
            print(task_1())
        case 2:
            print(task_2())
        case 3:
            print(task_3())
