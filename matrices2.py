import sys

string_a = input()
#ziskani listu integeru z inputu m, n
int_list = list(map(int, string_a.strip().split()))

m = int_list[0]
n = int_list[1]

if m == 0 or n == 0:
    sys.exit()

#import vsech radku do listu matrix_list
matrix_list = []
for i in range(m):
    x = str(input())
    x = list(map(int, x.strip().split()))
    matrix_list.append(x)

#hledani minima z list-listu
min = min(min(matrix_list))

#odecteni minima od vsech prvku v matici
for numbers in matrix_list:
    numbers[:] = [number - min for number in numbers]

#print vysledne matice
for row in matrix_list:
    for number in row:
        print(number, end=" ")
    print() #presun na novy radek

