# list itu kayak array di pemrograman lain

Data = [1, 4, 9, 16, 25, 36, 49, 64]
# mengakses list
Subdata1 = Data[0]
Subdata2 = Data[3]
Subdata3 = Data[-1]
Subdata4 = Data[-3]

# memotong list
Subdata5 = Data[0:4]
Subdata6 = Data[:4]
Subdata7 = Data[-5:]
# print(Data)
# print(Subdata7)

Data2 = [100, 200, 300, 400, 500, 600, 700, 800]
Data3 = Data + Data2
# print(Data3)

# merubah kontent dari list
Data[4] = 87
# print(Data)

# mengcopy list ke variable baru
# a = Data ---> bahaya jangan di gunakan
# a[4] = 87
# print(Data)
a = Data[:]  # ---> gunakan yang ini
a[4] = 87
# print(a)

# merubah content list dengan metoda slicing
Data[3:5] = [1020, 1203]
# print(Data)

# list dalam list
x = [Data, Data2]
# print(x)

# mengakses list dalam multidimensional list
y = x[0][5]
# print(y)

# method untuk list
Data.append(59)
# print(Data)

# function yang bisa kita gunakan kepada list
panjang_list = len(Data)
print(Data)
print(panjang_list)
