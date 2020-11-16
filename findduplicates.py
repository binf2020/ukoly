seznam = input().strip().split()
temporary = []

for cislo in seznam:
    if cislo in temporary:
        continue
    else:
        temporary.append(cislo)

if len(seznam) == len(temporary):
    print("No duplicates.")
else:
    print("The list contains duplicates.")