def divisors(num):
    try:
        if num < 0:
            raise ValueError("Ingresa un numero positivo")
        divisors = [i for i in range(1,num+1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return 0


def run():
    try:
        num = int(input('Ingresa un numero: '))
        print(divisors(num))
        print('Termino mi programa')
    except ValueError:
        print("Debes ingresar un numero")

if __name__ == '__main__':
    run()