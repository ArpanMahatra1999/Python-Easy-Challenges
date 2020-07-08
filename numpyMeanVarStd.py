  import numpy

numpy.set_printoptions(legacy="1.13")

ssi = input()
ssi = ssi.split()
N,M = int(ssi[0]),int(ssi[1])
my_array = []

for i in range(N):
    my_array.append([])
    values = input()
    values = values.split()
    for j in range(M):
        my_array[i].append(int(values[j]))
        
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
#print(format((numpy.std(my_array, axis = None)), '.12g'))
print(numpy.around( numpy.std(my_array, axis = None), 12))