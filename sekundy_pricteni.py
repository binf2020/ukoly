
# input v sekundach
hodiny = int(input("Zadejte pocet hodin:"))
minuty = int(input("Zadejte pocet minut:"))
sekundy = int(input("Zadejte pocet sekund:"))

soucet = sekundy + minuty*60 + hodiny*3600
print(f"{hodiny}:{minuty}:{sekundy}")

#pricteni dalsich sekund k nasemu casu
def pripocet_sekund():
    userinput = int(input("Zadejte pocet sekund k pricteni: \n"))
    sekundy = userinput+soucet
    hodiny = sekundy // 3600
    sekundy = sekundy % 3600
    minuty = sekundy // 60
    sekundy = sekundy % 60

    print(f"{hodiny} hodin, {minuty} minut, {sekundy} sekund")
pripocet_sekund()