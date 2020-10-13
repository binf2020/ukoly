maximum = int(input())
maximum2 = int(input())

if maximum2 > maximum :
    maximum, maximum2 = maximum2, maximum

while True:
    cislo = int(input())
    if cislo == -1:
        break

    if maximum == maximum2:
        if cislo >= maximum :
            maximum2 = maximum
            maximum = cislo
        else: maximum2 = cislo

    if cislo > maximum :
        maximum2 = maximum
        maximum = cislo

    if (cislo < maximum and cislo > maximum2) :
        maximum2 = cislo

print(maximum2)