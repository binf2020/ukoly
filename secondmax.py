
def secondMax(max1, max2):
    if max2 > max1:
        max1, max2 = max2, max1
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

a = int(input())
b = int(input())

result = secondMax(a, b)
print(result)

