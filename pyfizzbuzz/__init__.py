from itertools import cycle
from functools import reduce

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


def generator(n):
    curr = 1
    while curr <= n:
        yield 'Fizz' * (curr % 3 == 0) + 'Buzz' * (curr % 5 == 0) or curr
        curr += 1


def infinity(n):
    fizzes = cycle(['', '', 'Fizz'])
    buzzes = cycle(['', '', '', '', 'Buzz'])
    words = iter(map(lambda x: reduce(lambda i, j: str(i) + str(j), x), zip(fizzes, buzzes)))
    choice = lambda word, num: word or num
    return [choice(next(words), i) for i in range(1, n + 1)]


class FizzBuzz:
    fizz = "Fizz"
    buzz = "Buzz"

    def __init__(self, n):
        self.n = n

    def is_fizz(self):
        return self.n % 3 == 0

    def is_buzz(self):
        return self.n % 5 == 0

    def __str__(self):
        if self.is_fizz() and self.is_buzz():
            return self.fizz + self.buzz
        if self.is_fizz():
            return self.fizz
        if self.is_buzz():
            return self.buzz
        return str(self.n)


def object_oriented(n):
    return str(FizzBuzz(n))
