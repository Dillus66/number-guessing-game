from random import randrange
rand_nom = randrange(1, 6)
print (rand_nom)
guess_count = 3

while guess_count >0:
    guess = int(input('guess a number between 1 to 5\n'))
    if guess == rand_nom:
        print(f'{guess} is the correct answer')
        break
    else:
        print('wrong guess try again')
        guess_count -= 1

if guess_count == 0:
    print('you lose game over')
    print(f'correct answer was {rand_nom}')