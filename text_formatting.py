string = input()
num = 12 #pocet znaku na jeden radek

def TextFormat(string, width):
    #string split a pridavani slov na radek, 
    #dokud len(list(string)) <= num

    words = str.split(string) #rozdeleni stringu na slova
    text = [] #list listu(tj. lines)
    while True:
        char_count = 0 #pocet znaku, jenz appenduju slovama z words
        line = [] #jeden muj radek
        for word in words:
            char_count += len(word)
            if char_count <= num: #mene nez num
                line.append(f'{word} ')
                char_count += 1 #mezera mezi slovy
                continue
            elif char_count > num: #vice znaku nez num
                text.append(line)
                line = []
                char_count = len(word)
                line.append(f'{word} ')
                continue
            elif len(word) > num: #vyjimka pro dlouha slova
                text.append(f'{word} ')
                line = []
                char_count = 0
        text.append(line)
        break
    return text
            
text = (TextFormat(string, num))
for line in text:
    if line == []: #jestlize bude prvni slovo dlouhe, aby to neprintovalo prazdnou
        continue
    for word in line:
        print(word, end="")
    print()