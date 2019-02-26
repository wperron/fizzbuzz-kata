def functional(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "buzz"
    return str(n)


def in_range(n: int):
    return (
        'FizzBuzz' if n in range(0, 101, 15) else
        'Fizz' if n in range(0, 101, 3) else
        'Buzz' if n in range(0, 101, 5) else
        str(n)
    )


def composition(n):
    fizzes = [''] + ['', '', 'Fizz'] * 33 + ['']
    buzzes = [''] + ['', '', '', '', 'Buzz'] * 20
    nums = list(map(str, range(0, 101)))
    return fizzes[n] + buzzes[n] or nums[n]


fizzbuzz_lambda = lambda n: (
    'Fizz' * (n % 3 == 0) + 
    'Buzz' * (n % 5 == 0) or 
    str(n)
)


def arithmetic(n):
    options = [str(n), 'Fizz', 'Buzz', 'FizzBuzz']
    pattern = [3, 0, 0, 1, 0, 2, 1, 0, 0, 1, 2, 0, 1, 0, 0]
    return options[pattern[n % 15]]


def higher_order(n):
    fizz = lambda k: ( lambda j: "Fizz" + k("") ) if n % 3 == 0 else k
    buzz = lambda k: ( lambda j: "Buzz" + k("") ) if n % 5 == 0 else k
    identity = lambda x: x 

    return fizz(buzz(identity))(n)


class Fizz:
    def __call__(self, n):
        return "Fizz" * (n % 3 == 0) or ''

class Buzz:
    def __call__(self, n):
        return "Buzz" * (n % 5 == 0) or ''


def object_oriented(n):
    fizz = Fizz()
    buzz = Buzz()
    return fizz(n) + buzz(n) or n
