
base_pintada ='***'
base_clear = '   '
dimension = int(input('enter the dimension: '))
little_square_dimension = 3
for fila in range(dimension):
    if fila%2==0:
        for _ in range(little_square_dimension):
            prueba = ''
            for columna in range(dimension):
                if columna%2 ==0:
                    prueba += base_clear
                else:
                    prueba +=base_pintada
            print(prueba)
    else:
        for _ in range(little_square_dimension):
            prueba = ''
            for columna in range(dimension):
                if columna%2 ==0:
                    prueba += base_pintada
                else:
                    prueba +=base_clear
            print(prueba)

    