def generate_fibonacci(n: int) -> list:
    """
    Generate the first n Fibonacci numbers as a list.

    :param n: The number of Fibonacci numbers to generate.
    :return: A list containing the first n Fibonacci numbers.
    """
    if n <= 0:
        return []
    fibonacci = [0, 1]
    for _ in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:n]


print(generate_fibonacci(20))


def square_iterable(iterable: list) -> list:
    """
    Square each element in the iterable.

    :param iterable: An iterable (e.g., list, tuple) of numbers.
    :return: A list containing the squared values.
    """
    return list(map(lambda x: x ** 2, iterable))


def modulo_iterable(iterable: list, divisor: int) -> list:
    """
    Apply modulo operation to each element in the iterable.

    :param iterable: An iterable (e.g., list, tuple) of numbers.
    :param divisor: The divisor for the modulo operation.
    :return: A list containing the results of the modulo operation.
    """
    return list(map(lambda x: x % divisor, iterable))
