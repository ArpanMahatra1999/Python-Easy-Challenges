import numpy

N = int(input())
A,B = [],[]

for i in range(N):
    A.append([])
    string = input().split()
    for j in range(N):
        A[i].append(int(string[j]))

for i in range(N):
    B.append([])
    string = input().split()
    for j in range(N):
        B[i].append(int(string[j]))
        
A = numpy.array(A)
B = numpy.array(B)
print(A.dot(B))