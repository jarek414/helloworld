#     Przypisze zmiennej a1 wartość 10, zmiennej a2 wartość 15,
#     Utworzy zmienną sum_value, której nada wartość sumy zmiennych a1 i a2,
#     Utworzy zmienną quotus, której nada wartość ilorazu zmiennych a2 i a1,
#     Utworzy zmienną int_part, której nada wartość części całkowitej zmiennej quotus,
#     Wyświetli w terminalu wartości wszystkich zmiennych razem z ich typami.

a1 = 10
a2 = 15
sum_value = a1 + a2
quotus = a2 / a1
int_part = int(quotus // 1)

print(sum_value, type(sum_value))
print(quotus, type(quotus))
print(int_part, type(int_part))
