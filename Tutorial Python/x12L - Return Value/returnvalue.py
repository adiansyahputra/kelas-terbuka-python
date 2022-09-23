# fungsi dengan return value
def kuadrat(argumen):
    total = argumen**2
    print("nilai kuadrat dari", argumen, "adalah", total)
    return total


a = kuadrat(5)
print(a)

print("+"*100)

# fungsi dengan return value dan multiple argumen


def tambah(argumen1, argumen2):
    total = (argumen1+argumen2)
    print(argumen1, "+", argumen2, "=", total)
    return total


def kali(argumen1, argumen2):
    total = (argumen1*argumen2)
    print(argumen1, "x", argumen2, "=", total)
    return total


b = tambah(argumen2=5, argumen1=8)
c = kali(10, b)
print(b)
print(c)

# fungsi dengan return value dan multiple argumen


def tambah(argumen1, argumen2):
    total = (argumen1+argumen2)
    print(argumen1, "+", argumen2, "=", total)
    return [total, "inilist", 12, 9, 7]


b = tambah(argumen2=5, argumen1=8)
print(b)
