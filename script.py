# A program that gives you words to describe your day according to mood
import random

good = ['Blissful', 'cheerful', 'content', 'Ecstatic','calm']
moody = ['mediocre', 'middling', 'average', 'passable', 'grouchy']
bad = ['cranky', 'gloomy', 'glum', 'melancholy', 'sad']

def wordProd():
    mood = input("How are you feeling today? good, moody or bad: ")

    if mood == 'good':
        for word in good:
            print(random.sample(good, 3))

    elif mood == 'moody':
        for word in moody:
            print(random.sample(moody, 3))

    elif mood == 'bad':
        for word in bad:
            print(random.sample(bad, 3))
    else:
        print('Fuck you, I need an actual emotion you sick bastard!!!')

wordProd()
