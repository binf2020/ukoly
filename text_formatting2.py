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
            if len(word) >= num: #vyjimka pro dlouha slova
                text.append(line)
                text.append(word)
                line = []
                char_count = 0
            elif char_count <= num: #mene nez num
                line.append(word)
                char_count += 1 #mezera mezi slovy
                continue
            elif char_count > num: #vice znaku nez num
                text.append(line)
                line = []
                char_count = len(word) + 1 #rovnou to vklada mezeru za slovo na novem radku
                line.append(word)
                continue
        text.append(line)
        break
    return text

text = TextFormat(string, num)    

temp_list = list(map(' '.join, text))

def listToString(s):  
    str1 = " "  
    return (str1.join(s)) 

user_input = listToString(temp_list)

print(user_input)


    

""" def TextFormatPrint(str, width):
    #string split a pridavani slov na radek, 
    #dokud len(list(string)) <= num
    words = str.split(string) #rozdeleni stringu na slova
    line = ""
    for word in words:
        if len(word) >= num: #vyjimka pro dlouha slova
            if line != "":
                print(line)
                line = ""
            print(word)
        elif len(word) + len(line) > num - 1:
            print(line)
            word = line
        else:
            if line == "":
                line = word 
            else:
                line += " " + word
    if line != "":
        print(line) """    
            
""" text = (TextFormat(string, num))
for line in text:
    if line == []: #jestlize bude prvni slovo dlouhe, aby to neprintovalo prazdnou
        continue
    for word in line:
        print(word, end=" ")
    print() """

""" def TextFormat(string, width):
    #string split a pridavani slov na radek, 
    #dokud len(list(string)) <= num

    words = str.split(string) #rozdeleni stringu na slova
    text = [] #list listu(tj. lines)
    while True:
        char_count = 0 #pocet znaku, jenz appenduju slovama z words
        line = [] #jeden muj radek
        for word in words:
            char_count += len(word)
            if len(word) >= num: #vyjimka pro dlouha slova
                text.append(line)
                text.append(word)
                line = []
                char_count = 0
            elif char_count <= num: #mene nez num
                line.append(word)
                char_count += 1 #mezera mezi slovy
                continue
            elif char_count > num: #vice znaku nez num
                text.append(line)
                line = []
                char_count = len(word) + 1 #rovnou to vklada mezeru za slovo na novem radku
                line.append(word)
                continue
        text.append(line)
        break
    return text
 """