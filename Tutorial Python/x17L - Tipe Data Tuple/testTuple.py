import sys

dataList = [1, 2, 3, 4, 5, 6, "otong surotong", "markotong", False, 20.9]
dataTuple = (1, 2, 3, 4, 5, 6, "otong surotong", "markotong", False, 20.9)

ukuranDataList = sys.getsizeof(dataList)
ukuranDataTuple = sys.getsizeof(dataTuple)
print("ukuran data list: ", ukuranDataList)
print("ukuran data Tuple: ", ukuranDataTuple)
