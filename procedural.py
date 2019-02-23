import sys


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "buzz"
    return str(n)


if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) >= 2 else 100
    for i in range (1, limit + 1):
        print(fizzbuzz(i))
