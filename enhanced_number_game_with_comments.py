# Import the random module for generating random numbers
import random

# Function to get the difficulty level from the user
def get_difficulty_level():
    while True:
        # Ask the user to choose a difficulty level
        level = input("First, choose a difficulty level (easy, medium, hard): ")
        print('You have chosen {} level.'.format(level))
        
        # Provide feedback on the range of numbers based on the chosen level
        if level == 'easy':
            print ('You can guess between 1 to 10.')
        if level == 'medium':
            print ('You can guess between 1 to 50.')
        if level == 'hard':
            print ('You can guess between 1 to 100.')
        
        # Validate the user's input
        if level.lower() not in ['easy', 'medium', 'hard']:
            print("Invalid input. Please enter either 'easy', 'medium', or 'hard'.")
        else:
            return level.lower()

# Function to generate a random number based on the chosen difficulty level
def get_random_number(level):
    if level == 'easy':
        return random.randint(1, 10)
    elif level == 'medium':
        return random.randint(1, 50)
    else:  # hard level
        return random.randint(1, 100)

# Ask the user for their name
player_name = input("Hello, what is your name? ")
# Initialize the number of guesses to 0
number_of_guesses = 0
print('I\'m glad to meet you! {} \nLet\'s play a game with you, I will think a number, then you will guess, alright?'.format(player_name))

# Get the difficulty level from the user
level = get_difficulty_level()
# Generate a random number based on the chosen difficulty level
number = get_random_number(level)
# Initialize the score to 0
score = 0
print('Remember: You have only 3 chances. Guess a number:')

# Main game loop
while number_of_guesses < 3:
    try:
        # Ask the user for their guess
        guess = int(input())    
        # Increment the number of guesses
        number_of_guesses += 1  
    except ValueError: 
        # Handle non-integer inputs
        print("It's not an integer. Please enter an integer. Try again.") 
        continue

    # Check if the guess is too low, too high, or correct
    if guess < number:
        print('Your estimate is too low, go up a little. Try again!')
    elif guess > number:
        print('Your estimate is too high, go down a bit. Try again!')
    elif guess == number:
        # Increment the score if the guess is correct
        score = score + 1
        print( 'Congratulations {}, you guessed the number in {} tries! Your score so far is {}'.format(player_name, number_of_guesses, score))
        break

    # If the user has used up all their guesses, reveal the number
    if number_of_guesses == 3:
        print('Close but no cigar, you couldn\'t guess the number. \nWell, the number was {}.'.format(number))