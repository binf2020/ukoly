# input v sekundach


#output hodiny, minuty, sekundy
def prepocet():
    sekundy = int(input("Zadejte pocet sekund: \n"))
    hodiny = sekundy // 3600
    sekundy = sekundy % 3600
    minuty = sekundy // 60
    sekundy = sekundy % 60

    print(f"{hodiny} hodin, {minuty} minut, {sekundy} sekund")
prepocet()
