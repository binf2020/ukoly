def ReverseList():
    cisla = []
    while True:
        x = int(input())
        if x == -1:
            break
        cisla.append(x)
    cisla_reverse = cisla.reverse()
    for c in cisla_reverse:
        print(c, end=" ")

ReverseList()






    