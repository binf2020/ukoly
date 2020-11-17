vstup = input()
vstup = list(map(int, vstup.strip().split()))
rozdil = 1000000
a = 0
b = 0

vstup = sorted(vstup)

for i in range(len(vstup)-1, -1, -1):
    temp = vstup[i] - vstup[i-1]
    if temp < rozdil:
        rozdil = temp
        a = i
        b = i-1
    else:
        pass

