"""
Menguji Keanggotaan Tuple

Seperti halnya string dan list, kita bisa menguji apakah sebuah objek adalah anggota dari tuple atau tidak, yaitu dengan menggunakan operator in atau not in untuk kebalikannya.

"""

my_tuple = (1, 2, 3, "a", "b", "c")

# menggunakan in
# output: True
print(3 in my_tuple)

# output: False
print("e" in my_tuple)

# menggunakan not in
# output: True
print("k" not in my_tuple)
