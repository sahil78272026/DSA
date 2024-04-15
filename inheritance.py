class H():
    def m(self):
        print("H")

class G(H):
    def m(self):
        print("G")
        super().m()

class I(G):
    def m(self):
        print("I")
        super().m()


class F(H):
    def m(self):
        print("F")
        super().m()

class E(H):
    def m(self):
        print("E")
        super().m()

class D(F):
    def m(self):
        print("D")
        super().m()

class C(E, F, G):
    def m(self):
        print("C")
        super().m()

class B():
    def m(self):
        print("B")
        super().m()

class A(B, C, D):
    def m(self):
        print("A")
        super().m()

x = A()
x.m()