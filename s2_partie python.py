users = ['avg','juste_ozan','kévin']
password = 'abc'
words = ['house','bed','chair','table','computer','pen','window','room','screen','rooftop','garden','garage','kitchen','bathroom','toilet']
definitions = ['a building that people, usually one family, live in',
               'a large, rectangular piece of furniture, often with four legs, used for sleeping on',
               'a seat for one person that has a back, usually four legs, and sometimes two arms',
               'a flat surface, usually supported by four legs, used for putting things on',
               'an electronic machine that is used for storing, organizing, and finding words, numbers, and pictures, for doing calculations, and for controlling other machines',
               'a long, thin object used for writing or drawing with ink',
               'a space usually filled with glass in the wall of a building or in a vehicle, to allow light and air in and to allow people inside the building to see out',
               'a part of the inside of a building that is separated from other parts by walls, floor, and ceiling',
               'a flat surface in a cinema, on a television, or as part of a computer, on which pictures or words are shown',
               'the outside surface of the roof of a building',
               'a piece of land next to and belonging to a house, where flowers and other plants are grown, and often containing an area of grass',
               'a building where a car is kept, built next to or as part of a house',
               'a room where food is kept, prepared, and cooked and where the dishes are washed',
               'a room with a bath and/or shower and often a toilet',
               'a bowl-shaped device with a seat that you sit on or stand near when emptying the body of urine or solid waste, or another device used for this purpose']

    
for count in range(3):
    checkUser = 0
    print('')
    username = input('username: ')
    passwordUser = input('Password: ')
    lenUsers = len(users)
    for loop in range(lenUsers):
        if username == users[loop]:
            checkUser = 1
    
    if passwordUser == password and checkUser == 1:
        print('\nSuccessful Authentication')
        break
    elif count == 2:
        print('Sorry you type the wrong password too much time...')
        exit()
        
    elif passwordUser != password or checkUser != 1:
        print('Wrong username or password (',2-count,'retry left )\n')
    

 
def item():
    word = input('Enter a word you want to define: ')
    definition = input('Enter the definition of this word: ')
    print('')
    words.append(word)
    definitions.append(definition)
    otherItem = input('It\'s done, do you want to define another word ? (yes/no): ')
    if otherItem == 'yes':
        print('')
        item()
    else:
        main()
        
def define():
    wordChoice = input('Which word do you want to know the definition ?: ')
    lenWords = len(words)
    for loop in range(lenWords):
        if wordChoice == words[loop]:
            print('')
            print(words[loop],':',definitions[loop],'\n')
    otherDef = input('Do you want to see the definition of another word? (yes/no): ')
    if otherDef == 'yes':
        print('')
        define()
    else:
        main()
    
    
    
def main():
    triWords = sorted(words)
    print('\n\n--------------- Ɗιcтισηηαяу ---------------')
    print('\nHere are the words defined in the Ɗιcтισηηαяу:',triWords,'\n')
    userChoice = input('Do you want to define a word or to see a definition ? (word/def): ')
    if userChoice == 'word':
        item()
    elif userChoice == 'def':
        define()

main()