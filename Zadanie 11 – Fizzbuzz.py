# Używając pętli i konstrukcji z zakresem (1, 101) napisz program fizzbuzz, który dla każdej liczby od 1 do 100:
#
#     jeżeli liczba jest podzielna przez 3, wypisze na ekran Fizz
#     jeżeli liczba jest podzielna przez 5, program wypisze na ekran Buzz
#     jeżeli liczba jest podzielna przez 3 i 5, program wypisze na ekran FizzBuzz (przykładowo dla liczby 15 ma się
#     wypisać tylko FizzBuzz)
#     w przeciwnym wypadku program wypisze na ekran liczbę.

fizzbuzz_list = range(1, 101)

for i in fizzbuzz_list:
    if (i % 15) == 0:
        print("FizzBuzz")
    elif (i % 3) == 0:
        print("fizz")
    elif (i % 5) == 0:
        print("buzz")
    else:
        print(i)
