# Napisz program, który:
#
#     wyświetli na ekranie komunikat "Podaj pierwsze imię",
#     pobierze z klawiatury imię i zapisze go do zmiennej first_name,
#     wyświetli na ekranie komunikat "Podaj drugie imię",
#     pobierze z klawiatury drugie imię użytkownika i zapisze go do zmiennej second_name,
#     wyświetli na ekranie Takie same jeżeli imiona są takie same albo Różne jeżeli są różne.
first_name = input("podaj pierwsze immie")
second_name = input("podaj drugie imie")

if first_name == second_name:
    print("takie same imiona")
else:
    print("rozne")
