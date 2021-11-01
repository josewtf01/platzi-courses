def is_prime(num: int) -> bool:
    """Returns True if a number is prime or
    False if the number is not prime"""
    result = [x for x in range(2,num) if num % x == 0]
    return len(result) == 0

def run():
    num: int = 73
    num_is_prime: bool = is_prime(num)
    print(num_is_prime)


if __name__ == '__main__':
    run()