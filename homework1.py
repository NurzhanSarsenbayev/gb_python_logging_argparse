# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

import logging
import argparse

logging.basicConfig(filename='input_type.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')

def correct_input_type():
    while True:
        user_input = input('Type a number ')
        try:
            value = int(user_input)
            logging.info(f'User input was successfully converted into int : {user_input}')
            print(f'User input was successfully converted into int : {user_input}')
            return value
        except ValueError:
            try:
                value = float(user_input)
                logging.info(f'User input was successfully converted into float : {user_input}')
                print(f'User input was successfully converted into float : {user_input}')
                return value
            except ValueError:
                logging.info(f'Invalid user input : {user_input}')
                print('Your input is not a number')

#correct_input_type()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parser for user input')
    parser.add_argument("--prompt", type=str, default="Type a number: ", help="The prompt text to show the user")
    args = parser.parse_args()

    number = correct_input_type()
    print(f'You entered the number: {number}')