import random
import requests

def generate_password(memorable_word, birth_year, favorite_color, lucky_number):
    word_chars = list(memorable_word)
    birth_chars = list(birth_year)
    color_chars = list(favorite_color)
    number_chars = list(lucky_number)
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    selected_special_chars = random.sample(special_chars, 3)

    # Create a list of possible password structures
    password_structures = [
        [favorite_color, lucky_number, selected_special_chars[2], memorable_word, selected_special_chars[0]],
        [selected_special_chars[1], memorable_word, lucky_number, selected_special_chars[0], favorite_color],
        [favorite_color, selected_special_chars[0], selected_special_chars[1], lucky_number, memorable_word]
    ]

    password_structure = random.choice(password_structures)

    password = ""

    for category in password_structure:
        if isinstance(category, list):
            password += random.choice(category)
        else:
            password += category

    return password