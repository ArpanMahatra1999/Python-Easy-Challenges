import numpy

A = numpy.array(input().split())
B = numpy.array(input().split())

A = A.astype(int)
B = B.astype(int)

print(numpy.inner(A,B))
print(numpy.outer(A,B))