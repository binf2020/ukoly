a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = (a*d + b*c)
y = (b*d)

def nsd(a,b):
    if b == 0:
        return a
    else:
        return nsd(b, a%b)

def nsd2(a,b):
    while b > 0:
        a, b = b, a%b
    return x

d = nsd(x, y)

x = x // d
y = y // d

print(x)
print(y)