# method resolution order / multiple inheritance

class A:

    def show(self):
        print(f"ini adalah show A")


class B:

    def show(self):
        print(f"ini adalah show b")


class C(B, A):  # --> kalau method yang mau dipanggil sama maka dilihat urutannya di dalam kurung(duluan yang mana), sedangkan kalau punya maka dipakai yang dipunyai dulu
    pass


object = C()

object.show()
# help(object)

"""
Help on C in module __main__ object:

class C(A, B)
|  Method resolution order:
|      C
|      A
|      B
|      builtins.object
|  
|  Methods inherited from A:
|  
|  show(self)
|  
|  ----------------------------------------------------------------------
|  Data descriptors inherited from A:
|  
|  __dict__
|      dictionary for instance variables (if defined)
|  
|  __weakref__
"""
