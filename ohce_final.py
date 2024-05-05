import datetime

def greet(name):
    current_hour = datetime.datetime.now().hour
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

def start():
    start = input()
    try:
        ohce, name = start.split()
    except ValueError as e:
        return None
    if ohce != "ohce":
        return None
    return name


def handle_stop(name):
    return f'Adios {name}'
def main_loop():
    name = start()
    if name == None:
        return None
    print(greet(name))
    while True:
        word = input()
        if word == "stop!":
            print(handle_stop(name))
            break
        else:
            print(handle_word(word))
    return None

if __name__ == "__main__":
    main_loop()