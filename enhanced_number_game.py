import random
def get_difficulty_level():
    while True:
        level = input("First, choose a difficulty level (easy, medium, hard): ")
        print('You have chosen {} level.'.format(level))
        if level == 'easy':
            print ('You can guess between 1 to 10.')
        if level == 'medium':
            print ('You can guess between 1 to 50.')
        if level == 'hard':
            print ('You can guess between 1 to 100.')
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
print('I\'m glad to meet you! {} \nLet\'s play a game with you, I will think a number, then you will guess, alright?'.format(player_name))
level = get_difficulty_level()
number = get_random_number(level)
score = 0
print('Remember: You have only 3 chances. Guess a number:')

while number_of_guesses < 3:
    try:
        guess = int(input())
        number_of_guesses += 1
    except ValueError: 
        print("It's not an integer. Please enter an integer. Try again.") 
        continue

    if guess < number:
        print('Your estimate is too low, go up a little. Try again!')
    if guess > number:
       print('Your estimate is too high, go down a bit. Try again!')
    elif guess == number:
        score = score + 1
        print( 'Congratulations {}, you guessed the number in {} tries! Your score so far is {}'.format(player_name, number_of_guesses, score))
    else:
        print('Close but no cigar, you couldn\'t guess the number. \nWell, the number was {}.'.format(number))
    break