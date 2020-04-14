#     Napisz program, który obliczy kolejne potęgi liczby 2 dla wykładnika z przedziału od 0 do 10 włącznie.
#     Wyświetl wynik w postaci:

scuater = 0

for i in range(11):
    wynik = (2 ** scuater)
    print(f"{i} : {wynik}")
    scuater += 1
