class A:
    def methodA(self):
        print(f"ini adalah method a")


class B:
    def methodB(self):
        print(f"ini adalah method b")


class C(A, B):
    pass


pefiv = C()

pefiv.methodA()
pefiv.methodB()
