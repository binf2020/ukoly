#zjistujeme ordinerni cislo 
def val(c): 
    if c >= '0' and c <= '9': 
        return ord(c) - ord('0') 
    else: 
        return ord(c) - ord('A') + 10; 
  
#konverze z soustavy X do desitkove  
def toDeci(zapis,soustava):
    delka = len(zapis) 
    mocnina = 1 #budouci mocnina baze
    num = 0     #budouci vysledek
  
    #desitkovy ekvivalent je zapis[len-1]*1
    # + zapis[len-2]*soustava + zapis[len-3]
    # * soustava^2 . . .   
    for i in range(delka - 1, -1, -1): 
          
        #v pripade, ze je v inputu chyba 
        #a digit je vetsi nez soustava 
        if val(zapis[i]) >= soustava: 
            print('Invalid Number') 
            return -1
        num += val(zapis[i]) * mocnina 
        mocnina = mocnina * soustava 
    return num 

#zapis je nutny vest jako string!


def reVal(num): 
  
    if (num >= 0 and num <= 9): 
        return chr(num + ord('0')); 
    else: 
        return chr(num - 10 + ord('A')); 
  
# funkce pro obraceni stringu
def str_obrat(zapis): 
  
    len = len(zapis); 
    for i in range(int(len / 2)): 
        temporary = zapis[i]; 
        zapis[i] = zapis[len - i - 1]; 
        zapis[len - i - 1] = temporary; 
  
# funkce pro konverzi z decimalky
# na jakoukoli soustavu
def fromDeci(vysledek, soustava, inputNum): 
  
    index = 0; # pocatecni index
  
    # konverze inputNum pres opakovani
    # inputNum mod soustava
    while (inputNum > 0): 
        vysledek+= reVal(inputNum % soustava); 
        inputNum = int(inputNum / soustava); 
  
    # obraceni poradi digits ve vysledku
    vysledek = vysledek[::-1]; 
  
    return vysledek; 

vysledek = "" #protoze je to argument

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

sous1 = my_list[0]
x1= str(my_list[1])
sous2 = my_list[2]
x2 = str(my_list[3])
end_sous = my_list[4]

a = toDeci(x1, sous1)
b = toDeci(x2, sous2)


soucet = a + b
rozdil = a - b
soucin = a*b
cel_podil = a // b


soucet = fromDeci(vysledek, end_sous, soucet)
rozdil = fromDeci(vysledek, end_sous, rozdil)
soucin = fromDeci(vysledek, end_sous, soucin)
cel_podil = fromDeci(vysledek, end_sous, cel_podil)

print(soucet)
print(rozdil)
print(soucin)
print(cel_podil)