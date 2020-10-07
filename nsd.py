def nsd(a,b):
    if b == 0:
        return a
    else:
        return nsd(b, a%b)

print("Zadejte dve cisla a kalkulacka vam spocita nejvetsiho spolecneho delitele.")

promenna1 = int(input("Cislo 1:"))
promenna2 = int(input("Cislo 2:"))
print(nsd(promenna1, promenna2))