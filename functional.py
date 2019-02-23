import sys


def fizzbuzz(n: int, limit: int):
    return (
        'FizzBuzz' if n in range(0, limit + 1, 15) else
        'Fizz' if n in range(0, limit + 1, 3) else
        'Buzz' if n in range(0, limit + 1, 5) else
        str(n)
    )


if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) >= 2 else 100
    for i in range(1, limit + 1):
        print(fizzbuzz(i, limit))
