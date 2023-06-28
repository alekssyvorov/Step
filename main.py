def task_1():
    num_1 = int(input('Number '))
    print(num_1 // 10 % 10)
    print(num_1 % 10)


def task_2():
    num_1 = int(input('Number '))
    print(num_1 // 100)
    print(num_1 // 10)
    print(num_1 % 10)
    print(num_1 // 100 + num_1 // 10 + num_1 % 10)


def task_3():
    num_1 = input('Number 1')
    num_2 = input('Number 2')
    return int(num_1 + num_2)


def task_4():
    temperature_c = float(input('Input temperature '))
    return 9 / 5 * temperature_c + 32


if __name__ == "__main__":
    choice = int(input('Make you choice 1/2/3/4 '))
    match choice:
        case 1:
            task_1()
        case 2:
            print(task_2())
        case 3:
            print(task_3())
        case 4:
            print(task_4())
