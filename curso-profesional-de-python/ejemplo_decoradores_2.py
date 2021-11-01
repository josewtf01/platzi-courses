def with_custom_message(message):
    def with_message(function):
        print(f"{message}:")
        def wrapper(*args,**kwargs):
            function(*args,**kwargs)
        return wrapper
    return with_message

@with_custom_message("Hello")
def multiply(a,b):
    c = a* b
    print(f"The result of {a} * {b} is {c}")

def run():
    multiply(10,2)

if __name__ == '__main__':
    run()