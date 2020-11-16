string_a = input()
#ziskani listu integeru z inputu
int_list = list(map(int, string_a.strip().split()))
my_list = []

#odstraneni vsech int za -1, ktera uz neni v zadani
while True:
    for i in int_list:
        if i == -1:
            break
        else:
            my_list.append(i)
    break
#print vsech int v reverznim poradi na radek
for num in range(len(my_list) -1,-1,-1):
    print(my_list[num], end=" ")
    