from utils import get_average_age, get_average_gas, convert_temperature, get_delta_time, prime_number,\
    get_times_table, get_intersection, show_matrice, get_factorial

# Exercicios

# Selecione o numero do exercício que deseja testar:

testar_exercicio = 1

if testar_exercicio == 1:
    # 1: Calculo da média da idades

    i = 11
    j = 22
    k = 33
    x = 44
    y = 55

    idades = [i, j, k, x, y]

    media_idades = get_average_age(idades)

    print(f'A média das idades inseridas é {media_idades}')

elif testar_exercicio == 2:
    # 2: Calculo distancia x combustivel

    # Distancia
    a = 50

    # Combustivel
    b = 100

    media_combustivel = get_average_gas(a, b)

    print(f'A média de consume de combustivel é de {media_combustivel} por unidade de distância')

elif testar_exercicio == 3:
    # 3: Mostrar o menor numero

    # Numeros (a, b, c)

    numeros = [22, 3121, 995]

    print(f'O menor numero é {min(numeros)}')

elif testar_exercicio == 4:
    # 4: conversão de graus C para graus F

    graus_celsius = 22

    graus_fahrenheit = convert_temperature(graus_celsius)

    print(f'{graus_celsius} graus Celsius equivelem a {graus_fahrenheit} graus Fahrenheit')

elif testar_exercicio == 5:
    # 5: Mostrar se numeros são multiplos

    # Numeros:

    num_a = 4
    num_b = 2

    if num_a % num_b == 0:
        print(f'{num_a} é multiplo de {num_b}')
    else:
        print(f'{num_a} não é multiplo de {num_b}')

elif testar_exercicio == 6:
    # 6: Mostrar duração da partida

    a = '19:00'  # início da partida
    b = '20:43'  # final da partida

    duracao = get_delta_time(a, b)

    print(f'A partida durou {duracao}')

elif testar_exercicio == 7:
    # 7: Mostrar apenas numeros pares

    lista_num = [1, 2, 3, 4, 5]

    num_pares = [x for x in lista_num if x % 2 == 0]

    print(f'Os numeros pares da lista são: {num_pares}')

elif testar_exercicio == 8:
    # 8: Mostrar se numero é primo

    num_check = 6

    if prime_number(num_check):
        print(f'O numero {num_check} é primo!')
    else:
        print(f'O numero {num_check} não é primo!')

elif testar_exercicio == 9:
    # 9: Mostrar tabuada

    num_check = 7

    print(f'A tabuada de {num_check} é:\n')

    get_times_table(num_check)

elif testar_exercicio == 10:
    # 10: Mostrar fatorial do numero

    num_check = 8

    fatorial = get_factorial(num_check)

    print(f'O fatorial de {num_check} é {fatorial}')

elif testar_exercicio == 11:
    # 11: Intersecção das listas

    a = [1, 2, 3, 4]
    b = [1, 2, 5, 8]

    interseccao = get_intersection(a, b)

    print(f'A intersecção das listas é {interseccao}')

elif testar_exercicio == 12:
    # 12: Concatenação das listas

    a = [1, 2, 3, 4]
    b = [1, 2, 5, 8]

    print(f'A concatenação das listas é {a+b}')

elif testar_exercicio == 13:
    # 13: Mostrar matiz

    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    print('Sua matriz é:\n')

    show_matrice(a)

elif testar_exercicio == 14:
    # 14: Checar se a palavra é Palindromo

    palavra = 'Ovo'

    if palavra.lower() == palavra[::-1].lower():
        print(f'A palavra {palavra} é palindromo')
    else:
        print(f'A palavra {palavra} não é palindromo')
        print(f'{palavra.lower()} é diferente de {palavra[::-1].lower()}')
