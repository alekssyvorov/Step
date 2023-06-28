def task_1():
    num_1 = int(input('Number 1 '))
    num_2 = int(input('Number 2 '))
    num_3 = int(input('Number 3 '))
    return int(str(num_1) + str(num_2) + str(num_3))


def task_2():
    number = int(input('Input number '))
    result = 1
    while number > 0:
        temp = number % 10
        result *= temp
        number //= 10
    return result


def task_3():
    meters = float(input('Input meters '))
    cm = int(meters) * 100 + (meters - int(meters)) * 100
    dc = int(meters) * 10 + (meters - int(meters)) * 10
    mm = int(meters) * 1000 + (meters - int(meters)) * 1000
    mili = int(meters) * 0.000621371 + (meters - int(meters)) * 0.000621371
    return cm, dc, mm, mili


def task_4():
    h = float(input('Input height triangle '))
    ac = float(input('Input AC'))
    return 1 / 2 * h * ac


def task_5():
    number = int(input('Number '))
    result = ''
    while number > 0:  # 4521
        result += str(number % 10)
        number //= 10
    return int(result)


if __name__ == "__main__":
    choice = int(input('Make you choice 1/2/3/4/5'))
    match choice:
        case 1:
            print(task_1())
        case 2:
            print(task_2())
        case 3:
            print(task_3())
        case 4:
            print(task_4())
        case 5:
            print(task_5())
