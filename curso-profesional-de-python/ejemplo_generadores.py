def my_gen():
    """Un ejemplo de generadores"""

    print('Hello World')
    n = 0
    yield n

    print('Hello Heaven!')
    n = 1
    yield n

    print('Hello Hell!')
    n = 2
    yield n

def run():
    a = my_gen()
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))

if __name__ == "__main__":
    run()