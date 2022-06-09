lista_1 = ['h', 'e', 'l', 'l', 'o', '', 't', 'e', 'a', 'm']
lista_2 = ['h', 'e', 'l', 'l', 'o', '','w', 'o', 'r', 'l', 'd']

final_list = []

for i in lista_1:
    for j in lista_2:
        if i == j and (i not in final_list):
            final_list.append(i)
        else:
            pass


print(final_list)





""" number_of_users = int(input('Ingrese la cantidad de usuarios: '))

users = []


for i in range(number_of_users):
    user_information = {}
    print(f'user #{i+1} information')
    user_information['name'] = input('Name: ')
    user_information['age'] = input('Age: ')
    user_information['Adress'] = input('Adress: ')
    user_information['profession'] = input('Profession: ')
    user_information['phone_number'] = input('Phone Number: ')
    users.append(user_information)
    print('\n')
     """





