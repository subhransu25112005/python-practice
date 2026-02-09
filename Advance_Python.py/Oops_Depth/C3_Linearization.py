'''Python uses C3 Linearization to compute MRO.

Rules of C3:

Child class comes before parent

Parent order is preserved

No class appears twice'''

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())
