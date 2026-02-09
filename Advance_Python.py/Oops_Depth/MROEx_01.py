class A:
    def show(self):
        print("Class A")

class B(A):
    pass

obj = B()
obj.show()
#B → A → object
