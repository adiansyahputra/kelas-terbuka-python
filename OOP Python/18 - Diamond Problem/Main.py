class A:

    def show(self):
        print(f"ini adalah show A")


class B(A):

    def show(self):
        print(f"ini adalah show B")


class C(A):

    def show(self):
        print(f"ini adalah show C")


class D(B, C):
    pass


object = D()
object.show()
help(object)

"""
Help on D in module __main__ object:

class D(B, C)
|  Method resolution order:
|      D
|      B
|      C
|      A
|      builtins.object
|  
|  Methods inherited from B:
|  
|  show(self)
|  
|  ----------------------------------------------------------------------
|  Data descriptors inherited from A:
|  
|  __dict__
|      dictionary for instance variables (if defined)
"""
