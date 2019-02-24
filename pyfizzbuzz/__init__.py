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