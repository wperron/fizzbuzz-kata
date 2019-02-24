import sys
import argparse
import pyfizzbuzz

parser = argparse.ArgumentParser(description="Fizzbuzz program.")
parser.add_argument('--limit', '-l', dest='limit', type=int, help="Upper limit of FizzBuzz count.", nargs="?", default='100')
parser.add_argument('--alg', '-a', dest='alg', type=str, help="Which algorithm to use.", nargs='?', default='functional')

if __name__ == "__main__":
    args = parser.parse_args()
    print(f'Calculating FizzBuzz up to [ {args.limit} ] using [ {args.alg} ]')

    target = getattr(pyfizzbuzz, args.alg)
    for i in range(1, args.limit + 1):
        print(target(i))
