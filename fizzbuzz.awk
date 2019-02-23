# usage: echo {1..100} | tr ' ' '\n' | awk -f fizzbuzz.awk
$0 % 3 == 0 { printf "Fizz" }
$0 % 5 == 0 { printf "Buzz" }
$0 % 3 != 0 && $0 % 5 != 0 { printf $0 }
{ printf "\n" }
