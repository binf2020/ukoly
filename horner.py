def horner(a,x):
    h = 0

    for i in range(len(a)):
        h = h*x + a[i]
        print(h)
    return h
    

print(horner((5, 0,10,1),2))