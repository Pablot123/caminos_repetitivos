base_pintada ='***'
base_clear = '   '
dimension = int(input('enter the dimension: '))
little_square_dimension = 3 # this is the dimention of each little square 
#So my idea to solve this exercice was fill line by line, each row of the square had three lines
for row in range(dimension): #this lopp are for the rows, 
    if row%2==0: #the conditional is beacause the even rows starts by a white square
        for _ in range(little_square_dimension): #this lopp are for the lines
            line = ''
            for columna in range(dimension): #this loop are por the columns
                if columna%2 ==0:
                    line += base_clear #here we concatenate the string with '   '  
                else:
                    line +=base_pintada #here we concatenate the string with '***' 
            print(line)
    else: #the else is for the odds rows that starts by a black square
        for _ in range(little_square_dimension):
            line = ''
            for columna in range(dimension):
                if columna%2 ==0:
                    line += base_pintada
                else:
                    line +=base_clear
            print(line)

#PD: this excercise was cool but makes me get several gray hairs