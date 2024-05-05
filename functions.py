import datetime

def greet(time, name):
    current_hour = time
    if 20 <= current_hour <= 24 or 0 <= current_hour < 6:
        return f"¡Buenas noches {name}!"
    elif 6 <= current_hour < 12:
        return f"¡Buenos dias {name}!"
    elif 12 <= current_hour < 20:
        return f"¡Buenas tardes {name}!"

def handle_word(word):
    text_to_print = ""
    text_to_print = text_to_print + word[::-1]
    if (word == word[::-1]):
        text_to_print = text_to_print + "\n¡Bonita palabra!"

    return text_to_print


def handle_stop(name):
    return f'Adios {name}'

def main_loop(time, name, word_1, word_2, word_3, word_4):
    log = greet(time, name)
    words = [word_1, word_2, word_3, word_4]
    i = 0
    while True:
        word = words[i]
        if word == "stop!":
            log = log + f"\n{handle_stop(name)}"
            break
        else:
            log = log + f"\n{handle_word(word)}"
        i += 1
    return log

