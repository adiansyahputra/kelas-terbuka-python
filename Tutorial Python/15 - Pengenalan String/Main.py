data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Hallo apa kabar?"')
print("'Hallo apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string

print('ini adalah hari jum\'at')
print('g\'day, isn\'t it')

# backlash
print("C:\\user\\Ucup")

# tab
print("ucup\t\t\totong, semakin jauhan")

# backspace
print("ucup \botong, jadi deketan")

# newline
print("baris pertama. \nbaris kedua.")  # LF -> Line Feed -> unix, macos, linux
# CR -> Carriage Return -> commodore, lisp, acorn
print("baris pertama. \rbaris kedua.")
# CRLF -> Line Feed Carriage Return -> dipakai oleh windows
print("baris pertama. \r\nbaris kedua.")

# 3. String Literal atau Raw

# hati-hati
print("C:\new folder")
print(r"C:\new folder")
print(r"C:\n\t\r\t\s\bew folder")

# multiline literal string
print("""
Nama : Adiansyah Putra
Kelas : 11.1b.06
WKWKWKWKKWKWK
""")

# multiline literal string dan raw

print(r"""
Nama : Adiansyah Putra\r\das\ca\axa
Kelas : 11.1b.06asd\qs\dq\ef\q\a\c
WKWKWKWKKWKWK\asd\qw.dqs\dq.fq\sq\nasas
""")
