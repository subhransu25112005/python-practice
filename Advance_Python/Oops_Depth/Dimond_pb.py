class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.show()
#D → B → C → A → object
