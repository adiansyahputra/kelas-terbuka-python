"""
Fungsi adalah grup/blok program untuk melakukan tugas tertentu yang berulang. Fungsi membuat kode program menjadi reusable, artinya hanya di definisikan sekali saja, dan kemudian bisa digunakan berulang kali dari tempat lain di dalam program.
Fungsi memecah keseluruhan program menjadi bagian – bagian yang lebih kecil . Dengan semakin besarnya program, maka fungsi akan membuatnya menjadi lebih mudah diorganisir dan dimanage.
Sejauh ini, kita sudah menggunakan beberapa fungsi, misalnya fungsi print(), type(), dan sebagainya. Fungsi tersebut adalah fungsi bawaan dari Python. Kita bisa membuat fungsi kita sendiri sesuai kebutuhan.

Mendefinisikan Fungsi

Berikut adalah sintaks yang digunakan untuk membuat fungsi: 
def function_name(parameters):
    ---function_docstring---
    statement(s)

    return [expression]

Penjelasannya dari sintaks fungsi di atas:
1. Kata kunci def diikuti oleh function_name (nama fungsi), tanda kurung dan tanda titik
dua (:) menandai header (kepala) fungsi.
2. Parameter / argumen adalah input dari luar yang akan diproses di dalam tubuh fungsi.
3. "function_docstring" bersifat opsional, yaitu sebagai string yang digunakan untuk
dokumentasi atau penjelasan fungsi. “function_doctring” diletakkan paling atas setelah
baris def.
4. Setelah itu diletakkan baris – baris pernyataan (statements). Jangan lupa indentasi untuk
menandai blok fungsi.
5. return bersifat opsional. Gunanya adalah untuk mengembalikan suatu nilai expression
dari fungsi.
Berikut adalah contoh fungsi untuk menyapa seseorang.
"""


def sapa(nama):
    """
    fungsi ini untuk meanyapa seseorang sesuai nama yang dimasukkan sebagai parameter
    """
    print(f"Hi, {nama}. Apa kabar ?")
    return "hello world"


# pemanggilan fungsi
# output: Hi, Umar. Apa kabar ?
sapa("umar")

"""
Memanggil Fungsi
Bila fungsi sudah didefinisikan, maka ia sudah bisa dipanggil dari tempat lain di
dalam program. Untuk memanggil fungsi caranya adalah dengan mengetikkan nama fungsi berikut paramaternya. Untuk fungsi di atas, kita bisa melakukannya seperti contoh berikut:
>>> sapa('Galih') 
Hi, Galih. Apa kabar?
>>> sapa('Ratna') 
Hi, Ratna. Apa kabar?

"""

"""
Docstring
Docstring adalah singkatan dari documentation string. Ini berfungsi sebagai dokumentasi atau keterangan singkat tentang fungsi yang kita buat. Meskipun bersifat opsional, menuliskan docstring adalah kebiasaan yang baik. Untuk contoh di atas kita menuliskan docstring. Cara mengaksesnya adalah dengan menggunakan format namafungsi.__doc__
>>> print(sapa.__doc__)
<---Fungsi ini untuk menyapa seseorang sesuai nama yang dimasukkan sebagai parameter-->

"""
print(sapa.__doc__)

"""
Pernyataan Return
Pernyataan return digunakan untuk keluar dari fungsi dan kembali ke baris
selanjutnya dimana fungsi dipanggil. Adapun sintaks dari return adalah: return [expression_list]
return bisa berisi satu atau beberapa ekspresi atau nilai yang dievaluasi dan nilai tersebut akan dikembalikan. Bila tidak ada pernyataan return yang dibuat atau ekspresi dikosongkan, maka fungsi akan mengembalikan objek None. Perhatikan bila hasil keluaran dari fungsi sapa kita simpan dalam variabel.
>>> keluaran = sapa('Gani') 
>>> print(keluaran) None
"""

keluaran = sapa("gani")
print(keluaran)
