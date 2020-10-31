import numpy as np

string_a = input()
#ziskani listu integeru z inputu
int_list = list(map(int, string_a.strip().split()))

m = int_list[0]
n = int_list[1]

matrix_list = input()

def StrToMatrix(string, m, n):
    arr = np.array(string.split(), dtype=int)
    arr = np.reshape(arr, (m, n))
    return arr 

A = (StrToMatrix(matrix_list, m, n))

A = np.array(A)
min = np.amin(A)
B = A - min

for row in B:
    for number in row:
        print(number, end=" ")
    print()