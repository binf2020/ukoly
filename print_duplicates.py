seznam = input().strip().split()
temporary = []
duplicates = []

for cislo in seznam:
    if cislo in temporary:
        duplicates.append(cislo)
    else:
        temporary.append(cislo)

if len(seznam) == len(temporary):
    print("No duplicates.")
else:
    for d in duplicates:
        print(d, end=" ")