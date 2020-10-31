from collections import Counter


# prevzeti user inputu na x radcich
import sys

""" radky_ze_vstupu = []
for radek in sys.stdin:
    radky_ze_vstupu.append(radek)
 """
"""  
user_input = str(radky_ze_vstupu) """

user_input = input()

#  frekvence znaku od a do z v abecedach
Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
's','t','u','v','w','x','y','z']

en_freq = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153,
           0.772, 4.025, 2.406, 6.749,  7.507, 1.929, 0.095, 5.987, 6.327, 9.056,
           2.758, 0.978, 2.360, 0.150,  1.974, 0.074]

cz_freq = [8.421, 0.822, 0.740, 3.475, 7.562, 0.084, 0.092, 1.356, 6.073, 1.433,
           2.894, 3.802, 2.446, 6.468, 6.695, 1.906, 0.001, 4.799, 5.212, 5.727,
           2.160, 5.344, 0.016, 0.027, 1.043, 1.503]
           
# split inputu na jednotliva pismena bez dalsich znaku
def CharSplit(vstup):
    temporary = list(vstup)
    char_list = []
    #vybrat z toho jen pismena
    for i in temporary:
        i = i.upper()
        if ord(i) in range(65, 91): #pro tento ord to jsou uppercase letters
            char_list.append(i)
    return char_list


char_list = CharSplit(user_input)


# udelame si mapu procentuelniho zastoupeni znaku v nasem inputu
# jsou i jednodussi metody, ale nam se hodi,
# ze nam fce plive i nuly za char, ktere tam nejsou
def FindFreq(char_list):
    frequency_map=[]
    for i in range(0,26): 
        x = (char_list.count(Alphabet[i].upper()))
        x = x / len(char_list)
        frequency_map.append(x)
    return frequency_map

frequency_map= FindFreq(char_list)

# konverze pro pocitani do chi square
def ConToPerc(int_list):
    myInt = 100 # percentage
    int_list[:] = [x / myInt for x in int_list]

    return int_list
def ConFromPerc(int_list):
    myInt = 100 # percentage
    int_list[:] = [x * myInt for x in int_list]

    return int_list

#konvertujeme si tedy jak EN tak CZ mapu
en_freq = ConToPerc(en_freq)
cz_freq = ConToPerc(cz_freq)


def ChiSquare(observed, expected):
    temporary = 0
    for i in range(0, 25): #26 pismen, 26 volani
        chi_squared_stat = (((observed[i]-expected[i])**2)/expected[i])
        temporary += chi_squared_stat
    stat = temporary
    return stat


a = (ChiSquare(frequency_map, en_freq))
b = (ChiSquare(frequency_map, cz_freq))

print(f"Match with English: {a: .2f}")
print(f"Match with Czech: {b:.2f}")
if a<b:
    print("Text is in English")
else:
    print("Text is in Czech")











