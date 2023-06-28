def task_1():
    num_1 = float(input('Number 1 '))
    num_2 = float(input('Number 2 '))
    num_3 = float(input('Number 3 '))
    print(f"Summa = {num_1 + num_2 + num_3}\nMultiplication {num_1 * num_2 * num_3}")


def task_2():
    salary = float(input('Input salary '))
    cred = float(input('Input credit '))
    duty = float(input('Input duty '))
    print(f"{salary - cred - duty}")


def task_3():
    ac = float(input('Input AC'))
    bd = float(input('Input BD'))
    print(f"Area of a rhombus = {ac * bd / 2}")


if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
