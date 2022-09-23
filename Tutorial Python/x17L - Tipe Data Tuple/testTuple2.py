import timeit

dataList = timeit.timeit(stmt=[1, 2, 3, 4, 5, 6, 7], number=100000000)
dataTuple = timeit.timeit(stmt=(1, 2, 3, 4, 5, 6, 7), number=100000000)

print("ini adalah kecepatan list :", dataList)
print("ini adalah kecepatan tuple :", dataTuple)
