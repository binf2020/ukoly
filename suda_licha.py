
string_a = input()
#ziskani listu integeru z inputu
int_list = list(map(int, string_a.strip().split()))

suda = []
licha = []

#odstraneni vsech int za -1, ktera uz neni v zadani
while True:
    for i in int_list:
        if i == -1:
            break
        elif i % 2 == 0:
            suda.append(i)
        else:
            licha.append(i)
    break

for n in range(0, len(suda)):
    print(suda[n], end=" ")
for n in range(0, len(licha)):
    print(licha[n], end=" ")