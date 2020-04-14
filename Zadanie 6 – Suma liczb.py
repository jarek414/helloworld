# Napisz program, który policzy sumę wszystkich liczb od 0 do n, gdzie n jest podane przez użytkownika.
#
# Zadanie rozwiąż na dwa sposoby:
#
#     używając pętli,
#     korzystając z wbudowanych w Pythona funkcji: range i sum.

print("liczymy sume licz od zera do twojej liczby")
your_number = int(input("please input your number"))

sum_value = 0
for i in range(your_number):
    sum_value = sum_value + i
    print(sum_value)
