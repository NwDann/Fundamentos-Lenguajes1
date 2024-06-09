
class A():
    def hablar(self):
        print("hola q tal desde A")
        
class B(A):
    def hablar(self):
        print("hola q tal desde B")
    
class C(A):
    def hablar(self):
        print("hola q tal desde C")
    
class D(B, C):
    def hablar(self):
        print("hola q tal desde D")


d = D()
d.hablar()