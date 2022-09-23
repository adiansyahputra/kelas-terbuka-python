"""
Perulangan menggunakan while akan menjalankan blok pernyataan terus menerus selama kondisi bernilai benar. Adapun sintaks dari perulangan menggunakan while adalah:

while expression:
    statement (s)

Di sini, statement (s) bisa terdiri dari satu baris atau satu blok pernyataan. Expression merupakan ekspresi atau kondisi apa saja, dan untuk nilai selain nol dianggap True. Iterasi akan terus berlanjut selama kondisi benar. Bila kondisi salah, maka program akan keluar dari while dan lanjut ke baris pernyataan di luar while. 
"""

count = 0

while count < 5:
    print("The count is:", count)
    count += 1
print("good bye!")

"""
infinite loop

Sebuah kondisi dimana loop selalu benar dan tidak pernah salah disebut loop tidak terbatas (infinite loop). Terkadang hal ini menjadi masalah. Tapi sering juga infinite loop berguna, misalnya untuk program client/server dimana server perlu menjaga komunikasi tetap hidup dan tidak terputus. Pada contoh program while di atas, bila kita lupa menuliskan kode count = count + 1, maka akan jadi infinite loop. Hasilnya akan jadi seperti berikut:
The count is: 0
The count is: 0
The count is: 0
The count is: 0
The count is: 0
Traceback (most recent call last):
File "<pyshell#4>", line 2, in <module>
print('The count is:', count)
File "C:\Python34\lib\idlelib\PyShell.py", line 1344, in write return self.shell.write(s, self.tags)
KeyboardInterrupt
Kita perlu menekan CTRL+C untuk menghentikan program.

"""
