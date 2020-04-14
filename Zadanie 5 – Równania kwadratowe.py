# Napisz program do pomocy licealistom w liczeniu pierwiastków równań kwadratowych. Program ma:
#
#     wyświetlić na ekranie komunikat: Równanie w postaci a*x**2 + b*x + c == 0,
#     wyświetlić na ekranie komunikat: Podaj a,
#     pobrać wartość od użytkownika i zapisać ją do zmiennej a (pamiętaj o rzutowaniu na odpowiedni typ),
#     wyświetlić na ekranie komunikat: Podaj b,
#     pobrać wartość od użytkownika i zapisać ją do zmiennej b (pamiętaj o rzutowaniu na odpowiedni typ),
#     wyświetlić na ekranie komunikat: Podaj c,
#     pobrać wartość od użytkownika i zapisać ją do zmiennej c (pamiętaj o rzutowaniu na odpowiedni typ),
#     policzy deltę,
#     jeśli delta > 0, policzyć wartości x_1 i x_2, a następnie wyświetlić je w postaci:
print("Równanie w postaci a*x**2 + b*x + c == 0 ")
a = int(input("prosze podaj wartosc a"))
b = int(input("prosze podaj wartosc b"))
c = int(input("prosze podaj wartosc c"))

delta = b ** 2 - 4 * a * c
print(delta)
if delta > 0:
    x1 = (-b - (delta * 0.5)) / (2 * a)
    x2 = (-b + (delta * 0.5)) / (2 * a)
    print(x1, x2)
elif delta == 0:
    z1 = -b / (2 * a)
    print(z1)
else:
    print(" delta jest ujemna ")
