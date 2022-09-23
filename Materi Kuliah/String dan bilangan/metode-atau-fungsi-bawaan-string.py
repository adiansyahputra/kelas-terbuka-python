"""
Metode / Fungsi Bawaan String
String memiliki banyak fungsi bawaan. format() yang kita bahas di atas hanya salah satu darinya. Fungsi atau metode lainnya yang sering dipakai adalah join(), lower(), upper(), split(), startswith(), endswith(), replace() dan lain sebagainya.
>>> "Universitas Bina Sarana Informatika".lower() 'universitas bina sarana informatika'
>>> " Universitas Bina Sarana Informatika ".upper() 'UNIVERSITAS BINA SARANA INFORMATIKA'
>>> "I love programming in Python".split() 
['I', 'love', 'programming', 'in', 'Python'] 
>>> "I love Python".startswith("I")
True
>>> "Saya belajar Python".endswith("on") 
True
>>> ' - '.join(['I', 'love', 'you'])
I - love - you
>>> "Belajar Java di BSI".replace('Java', 'Python') 
'Belajar Python di BSI'

"""
print("Universitas Bina Nusantara".lower())
print("Universitas Bina Nusantara".upper())
print("I love programming in python".split())
print("I love programming in python".startswith("I"))
print("I love programming in python".endswith("n"))
print("-".join(["I", 'Love', "You"]))
print("Belajar C di BSI".replace("C", "Python"))
