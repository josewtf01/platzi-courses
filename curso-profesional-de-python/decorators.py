from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args,**kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"Pasaron {time_elapsed.total_seconds()} segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 1_000_000):
        pass

@execution_time
def suma(a: int, b: int ) -> int:
    return a + b


@execution_time
def saludo(nombre="Cesar"):
    print(f"Hola {nombre}")



def run():
    random_func()
    suma(5,6)
    saludo("Facundo")



if __name__ == '__main__':
    run()