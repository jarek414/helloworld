# Napisz program, który:
#
#     przyjmie od użytkownika informację, ile liczb ten chce wprowadzić,
#     przyjmie n liczb (gdzie n - podane przez użytkownika),
#     zapisze wprowadzone przez użytkownika liczby w liście w zmiennej numbers,
#     policzy ich sumę i średnią,
#     wypisze na ekran te liczby i czy suma jest większa od średniej:
ilosc = int(input("ile liczb zemiezasz podac?"))
numbers_list = []
for i in range(ilosc):
    additional_number = int(input("prosze podaj kolejny numer"))
    numbers_list.append(additional_number)

suma_liczb = (sum(numbers_list))
srednia_liczb = sum(numbers_list) / ilosc

print(f"wprowadzone liczby {numbers_list}")
print(f"suma : {suma_liczb}")
print(f"srednia : {srednia_liczb}")
if suma_liczb > srednia_liczb:
    print("suma jest wieksza")
elif suma_liczb < srednia_liczb:
    print("srednia jest wieksza")
else:
    print("srednia jest rowna sumie ")
