vstup = int(input())
podMaximum = None
maximum = vstup
while vstup != -1:
    if vstup > maximum:
        podMaximum = maximum
        maximum = vstup
    elif vstup < maximum:
        if podMaximum is None:
            podMaximum = vstup
        elif vstup > podMaximum:
            podMaximum = vstup
    vstup = int(input())
print(podMaximum)
exit()