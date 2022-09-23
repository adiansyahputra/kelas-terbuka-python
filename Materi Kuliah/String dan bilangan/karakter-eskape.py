"""
Karakter Escape
Kalau kita hendak mencetak string: He said, "What's there?" kita tidak bisa menggunakan tanda kutip tunggal maupun ganda. Bila kita melakukannya, akan muncul pesan error SyntaxError karena teks berisi kutip tunggal dan ganda.
>>> print("He said, "What's there?"") ...
SyntaxError: invalid syntax
>>> print('He said, "What's there?"') ...
SyntaxError: invalid syntax
Untuk hal seperti ini kita bisa menggunakan tanda kutip tiga atau menggunakan karakter escape. Karakter escape dimulai dengan tanda backslash \. Interpreter akan menerjemahkannya dengan cara berbeda dengan string biasa. Solusi untuk error di atas adalah sebagai berikut:
"""

# menggunakan kutip tiga
print("""He said, What's there ? """)

# menggunakan karakter escape untuk tanda kutip tunggal
print('He said, What\'s there ?')

# menggunakan karakter escape untuk tanda kutip ganda
print("He said, what\'s there ?")

"""
Berikut adalah daftar karakter escape yang didukung oleh Python.
Karakter Escape -------------- Deskripsi
"""

# \newline  -->>>               Backslash dan newline diabaikan

# \\        -->>>               Backslash

# \’        -->>>               Kutip tunggal

# \”        -->>>               Kutip ganda

# \a        -->>>               ASCII bel

# \b        -->>>               ASCII backscape

# \f        -->>>               ASCII formfeed

# \n        -->>>               ASCII linefeed

# \r        -->>>               ASCII carriage return

# \t        -->>>               ASCII tab horizontal

# \v        -->>>               ASCII tab horizontal

# \ooo      -->>>               karakter dengan nilai oktal oo

# \xHH      -->>>               karakter dengan nilai heksadesimal HH

# Berikut ini adalah beberapa contohnya:

# >>> print("C:\\Python34\\Lib")
# C:\Python34\Lib

# >>> print("Ini adalah baris pertama\nDan ini baris dua")
# Ini adalah baris pertama
# Dan ini baris dua

# >>> print("Ini adalah \x48\x45\x58")
# Ini adalah HEX

# Raw String untuk Mengabaikan Karakter Escape

# Kadang kala kita perlu untuk mengabaikan karakter escape yang ada dalam string. Kita bisa melakukannya dengan meletakkan huruf r atau R sebelum tanda kutip string.

# >>> print("This is \x61 \ngood example")
# This is a good example

# >>> print(r"This is \x61 \ngood example")
# This is \x61 \ngood example

print(r"This is \x61 \ngood example")
print("Ini adalah \x48\x45\x58")
print("This is \x61 \ngood example")
