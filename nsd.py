def nsd(x,y):
    if x > y:
        x,y = y, x
        continue
        z = y%x
        while True:
            if z == 0:
                print(x)
            
            elif x%z == 0 and y%z == 0:
                print(z)
                
            else:
                print("1")
                

print("Zadejte dve cisla a kalkulacka vam spocita nejvetsiho spolecneho delitele.")

promenna1 = int(input("Cislo 1:"))
promenna2 = int(input("Cislo 2:"))
nsd(promenna1, promenna2)