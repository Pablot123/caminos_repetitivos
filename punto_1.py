#'Dictionary' with tuples of articles and criatures
articles_species = [('un','Kraken'),('unas', 'Sirenas'),('una','Ballena'),
                    ('un', 'Hipocampo'), ('una','Macaraprono'), ('un', 'Pulpo'),
                    ('unos', 'Leviatanes'), ('unas', 'Hidras')]

#'Dictionary' with tuples of articles and directions
articles_direction = [('a', 'babor'),('a', 'estribor'),('por la', 'popa'),('por la', 'proa')]

flag = True #Variable to control the while loop
while flag:
    criature_exist = False # variable to control if the criature enter by the user are in the 'dictionary'
    direction_exist = False # variable to control if the direction enter by the user are in the 'dictionary'
    
    #Here we take as input the criature and the direction at the same time 
    # its important that this two are separated by a space but between this two there may be conectors
    # like  'kraken and proa' or 'Kraken y proa'.
    # then I split the text and only take the first and the last element that corresponds the 
    # criature and the direction respectively.
    criature_direction = (input('Enter the name of the criature followed by the direction: ')). split(' ')
    # We normilize the input of the creature tu match with the dictionary, we do the same with the direction
    # in this case we first lower the word and then capitalize it
    criature = criature_direction[0].lower().capitalize()
    direction = criature_direction[-1].lower()
   
    inicial_text = '¡Ahoy!capitán, '
    #The first conditional helps to stop the program with the word 'stop', we normalize the word 
    #so the user dont need to we worried of the way to write the word
    if criature_direction[0].lower() != 'stop':
        for article, specie in articles_species: #this loop is to search the criature on the distionary
            if specie == criature:
                criature_exist = True 
                inicial_text += f'{article} {specie} ' #here We concatenate the text to print
                break
        
        for article_d, dir in articles_direction: #this loop is to search the direction on the distionary
            if dir == direction:
                direction_exist = True
                inicial_text += f'{article_d} {direction}.'#here We concatenate the text to print
                break
        # this conditional manage the existance of the creature or the direction
        if criature_exist and direction_exist: 
            print(inicial_text)
        elif not(criature_exist) and direction_exist:
            print('Ups we don\'t know that criature')
        elif criature_exist and not(direction_exist):
            print('Ups the direction dosen\'t exist')
        else:
            print('Ups the direction and the criature dosen\'t exist')
    else:
        flag = False #if the word 'stop' is typed this flag end the loop
    

