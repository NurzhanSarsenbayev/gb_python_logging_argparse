from random import randint
import logging
import argparse
# from homework1 import correct_input_type

logging.basicConfig(filename='guessing_game.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')

def correct_input_type_int(prompt = None): # Сначала хотел импортировать метод из первой задачи, но потом решил просто его немного упростить

    while True :
        print(prompt)
        user_input = input('Type a number\n')
        try:
            value = int(user_input)
            logging.info(f'User input was successfully converted into int : {user_input}')
            print(f'User input was successfully converted into int : {user_input}')
            return value
        except ValueError:
            logging.info(f'Invalid user input : {user_input}')
            print('Your input is not int number')

def get_min_max_numbers():
    while True:
        min_number = correct_input_type_int('Minimum number?')
        max_number = correct_input_type_int('Maximum number?')
        if min_number < max_number:
            return min_number, max_number
        else:
            logging.warning(f'Minimum number {min_number} is not less than maximum number {max_number}')
            print('Minimum number must be less than maximum number. Please try again.')
def guessing_game():

    min_number,max_number = get_min_max_numbers()
    tries = correct_input_type_int('Number of tries?')
    number = randint(min_number,max_number)
    print(f'For testing purposes, answer is {number}')
    while tries > 0:
        try:
            guess = int(input(f'Guess number? You have {tries} tries left\n'))
            if guess == number:
                logging.info(f'User correctly guessed {number} and had {tries} tries left')
                print('Victory')
                return True
            else:
                if number < guess:
                    print('Lower')
                else:
                    print('Higher')
                tries -= 1
                logging.debug(f'User guessed {guess}. Tries left: {tries}')
        except ValueError:
            logging.warning('Wrong type for input. Must be int.')
            print('Wrong type for input. Must be int. Try again')
    print('Out of tries')
    logging.info(f"User couldn't guess {number}")
    return False

#guessing_game()

if __name__ ==  '__main__':
    parser = argparse.ArgumentParser(description='Parser for user input of function parameters.')
    parser.add_argument("--prompt", type=str, default="", help="The prompt text to show the user")
    args = parser.parse_args()

    result = guessing_game()
    print(f'Did you win? {result}')

