# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

import logging
import argparse

# Configure logging
logging.basicConfig(filename="dict_get_function.log", level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')


def error_get_func(dictionary, user_input_value, def_val=None):
    try:
        logging.info(f"Dictionary provided: {dictionary}")

        if user_input_value.replace('.', '', 1).isdigit():
            try:
                user_input = int(user_input_value)
            except ValueError:
                try:
                    user_input = float(user_input_value)
                except ValueError:
                    logging.warning('Input is not int or float. Defaulting to string.')
                    user_input = user_input_value
        else:
            user_input = user_input_value

        logging.info(f"User input: {user_input}")
        value = dictionary[user_input]
        logging.info(f"Successfully returned value from dictionary. {user_input}: {value}")
        return value
    except KeyError:
        logging.error(f"Key {user_input} not found in dictionary. Returning default value {def_val}.")
        return def_val


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Retrieve a value from a dictionary based on a user-provided key.')
    parser.add_argument('--key', type=str, required=True, help='The key whose value you wish to return.')
    parser.add_argument('--default', type=str,
                        help='The default value to return if the key is not found in the dictionary.')

    args = parser.parse_args()

    sample_dict = {1: 'hello', 2: 'world', 'name': 'Alice', 3.5: 'float key'}

    result = error_get_func(sample_dict, args.key, args.default)
    print(f'Result: {result}')