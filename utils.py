import datetime


def get_average_age(ages):
    total_age = sum(ages)
    average_age = total_age/len(ages)

    return average_age


def get_average_gas(distance, gas):
    average_gas = gas/distance

    return average_gas


def convert_temperature(degrees):
    converted_degress = (degrees/(5/9)) + 32

    return converted_degress


def get_delta_time(initial_time_str, end_time_str):
    initial_time = datetime.datetime.strptime(initial_time_str, '%H:%M')
    end_time = datetime.datetime.strptime(end_time_str, '%H:%M')
    delta_time = end_time - initial_time

    return delta_time


def prime_number(number):
    prime_flag = True

    if number < 2:
        return False
    elif number <= 3:
        return True

    for x in range(2, number):
        if number % x == 0:
            prime_flag = False
            break

    return prime_flag


def get_times_table(number):
    for x in range(11):
        print(f'{number} x {x} = {number*x}')


def get_factorial(number):
    total = 1

    if number == 0:
        return 1

    for x in range(1, number + 1):
        total = total * x

    return total


def get_intersection(list_a, list_b):
    inter_list = [x for x in list_a if x in list_b]

    return inter_list


def show_matrice(matrice):
    for row in matrice:
        elementos = [str(x) for x in row]
        elementos = ' '.join(elementos)
        linha = f'|{elementos}|'
        print(f'{linha}')
