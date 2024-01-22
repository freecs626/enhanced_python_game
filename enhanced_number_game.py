import random
def get_difficulty_level():
    while True:
        level = input("Choose a difficulty level (easy, medium, hard): ")
        if level.lower() not in ['easy', 'medium', 'hard']:
            print("Invalid input. Please enter either 'easy', 'medium', or 'hard'.")
        else:
            return level.lower()

def get_random_number(level):
    if level == 'easy':
        return random.randint(1, 10)
    elif level == 'medium':
        return random.randint(1, 50)
    else:  # hard level
        return random.randint(1, 100)

player_name = input("Hello, what is your name? ")
number_of_guesses = 0
level = get_difficulty_level()
number = get_random_number(level)
score = 0


print('I\'m glad to meet you! {} \nLet\'s play a game with you, I will think a number then you will guess, alright? \nDon\'t forget! You have only 3 chances so guess:'.format(player_name))

while number_of_guesses < 3:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your estimate is too low, go up a little!')
    if guess > number:
       print('Your estimate is too high, go down a bit!')
    if guess == number:
        break
    

if guess == number:
    score = score + 1
    print( 'Congratulations {}, you guessed the number in {} tries! Your score so far is {}'.format(player_name, number_of_guesses, score))
else:
    print('Close but no cigar, you couldn\'t guess the number. \nWell, the number was {}.'.format(number))