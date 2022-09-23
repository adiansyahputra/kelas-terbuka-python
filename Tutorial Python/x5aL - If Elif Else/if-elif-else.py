# nilai1 = 75
# nilai2 = 20
# if nilai1 == 75:
#     print("nilai anda :", nilai1)
#     if nilai2 == 20:
#         print("nilai anda :", nilai2)

nilai = 29

if nilai == 49:  # equal eksplisit
    print("nilai anda :", nilai)

if nilai != 49:  # not equal eksplisit
    print("nilai anda bukan : 49")

print(39 * "=")

nilai = 90

if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai < 80:
    print("nilai anda adalah B")
elif 60 <= nilai < 70:
    print("nilai anda adalah C")
elif 50 <= nilai < 60:
    print("nilai anda adalah D, Lakukan Perbaikan")
else:
    print("maaf anda tidak lulus mata kuliah ini")

print(39 * "+")

jual = ["bakwan", "lontong", "combro", "misro", "tahu", "risol"]
beli = "donat"

if beli in jual:
    print('mamang bilang, "ya, saya jual', beli, '"')

if not beli in jual:
    print('"saya gak jual', beli, '"')

karakter = "g"
if karakter in beli:
    print("ada", karakter, "di", beli)
else:
    print("tidak ada", karakter, "di", beli)
