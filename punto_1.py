articles_species = [('un','Kraken'),('unas', 'Sirenas'),('una','Ballena'),
                    ('un', 'Hipocampo'), ('una','Macaraprono'), ('un', 'Pulpo'),
                    ('unos', 'Leviatanes'), ('unas', 'Hidras')]


articles_direction = [('a', 'babor'),('a', 'estribor'),('por la', 'popa'),('por la', 'proa')]

flag = True
while flag:
    criature_exist = False
    direction_exist = False
    criature_direction = (input('Enter the name of the criature followed by the direction: ')). split(' ')
    criature = criature_direction[0].lower().capitalize()
    direction = criature_direction[-1].lower()
    #criature = (input('Name of the criature: ')).lower().capitalize()
    #direction = (input('direction of the seen criature: ')).lower()
    inicial_text = '¡Ahoy!capitán, '
    # if criature != 'Stop' or direction != 'stop':
    if criature_direction[0].lower() != 'stop':
        for article, specie in articles_species:
            if specie == criature:
                criature_exist = True
                inicial_text += f'{article} {specie} '
                break
        
        for article_d, dir in articles_direction:
            if dir == direction:
                direction_exist = True
                inicial_text += f'{article_d} {direction}.'
                break

        if criature_exist and direction_exist:
            print(inicial_text)
        elif not(criature_exist) and direction_exist:
            print('Ups we don\'t know that criature')
        elif criature_exist and not(direction_exist):
            print('Ups the direction dosen\'t exist')
        else:
            print('Ups the direction and the criature dosen\'t exist')
    else:
        flag = False
    

