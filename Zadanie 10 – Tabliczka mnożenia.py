#     Napisz program, który pobierze od użytkownika liczbę n (z przedziału 1-10).
#     Następnie wygeneruj dla tabliczkę mnożenia dla podanej liczby (patrz przykład poniżej).

your_number = int(input("please input your number form range 1 - 10"))

for i in range(1, 11):
    wynik = i * your_number
    print(f" {i} * {your_number} = {wynik}")
