cisla = []
x = 0
while True:
    x = int(input())
    if x == -1:
        break
    cisla.append(x)

def secondMax(max1, max2):
    while True:
        cislo = int(input())
        if cislo == -1:
            break
        elif cislo > max1:
            max2 = max1
            max1 = cislo
        elif max2 < cislo < max1:
            max2 = cislo
    return max2

a = float('-inf')
b = float('-inf')

secondMax(a, b)

k = int(input())
cisla.sort(reverse=True)
print(cisla[k-1])