string = input()
num = int(input())

def TextFormatPrint(string, num):
    words = string.split() #rozdeleni stringu na slova
    line = ""
    for word in words:
        if len(word) >= num: #vyjimka pro dlouha slova
            if line != "":
                print(line)
                line = ""
            print(word)
        elif len(word) + len(line) > num - 1:
            print(line)
            line = word
        else:
            if line == "":
                line = word 
            else:
                line += " " + word
    if line != "":
        print(line)

TextFormatPrint(string, num)

