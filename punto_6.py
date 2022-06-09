lista_1 = ['h', 'e', 'l', 'l', 'o', '', 't', 'e', 'a', 'm']
lista_2 = ['h', 'e', 'l', 'l', 'o', '','w', 'o', 'r', 'l', 'd']

final_list = []
# we iterate the first letter with all the other letters in the next list
for i in lista_1:
    for j in lista_2:
        # this conditinitial ask if the letters are the same and the letter
        #  are not in the final list(this means that the letter is not repeated)
        # add the letter to le list. 
        if i == j and (i not in final_list): 
            final_list.append(i)
        else:
            pass

print(final_list)

