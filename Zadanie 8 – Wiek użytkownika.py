# Napisz program, który:
#
#     wyświetli na ekranie komunikat "Podaj swoje imię: ",
#     pobierze z klawiatury imię użytkownika i zapisze go do zmiennej name,
#     wyświetli na ekranie komunikat "Podaj rok swojego urodzenia: ",
#     pobierze z klawiatury roku urodzenia użytkownika i zapisze go do zmiennej year,
#     zamieni rok urodzenia użytkownika na liczbę,
#     obliczy aktualny wiek użytkownika i zapisze go do zmiennej age,
#     wyświetli na konsoli komunikat, w którym poda imię i aktualny wiek użytkownika: Użytkownik: <name> jest w wieku <age> lat.
#
# UWAGA: zakładamy, że użytkownik jako rok swojego urodzenia poda poprawną liczbę!

import datetime


rok = datetime.datetime.now().year

name = input("prosze podaj swoje imie")
year = int(input(" prosze podaj swoj rok urodzenia"))
age = rok - year

print(f"Użytkownik: {name} jest w wieku {age} lat ")

