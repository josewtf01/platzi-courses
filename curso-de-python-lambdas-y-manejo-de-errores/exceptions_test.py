def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacia")
    except ValueError as ve:
        print(ve)
        return False
    else:
        return string == string[::-1]


    return string == string[::-1]

def run():
    try:
        print(palindrome(""))
    except TypeError:
        print("Solo se pueden ingresar strings")


if __name__ == '__main__':
    run()