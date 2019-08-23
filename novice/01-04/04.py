class A:
    def truth(self):
        return 'All numbers are even'
    
class B(A):
    pass

class C(A):
    def truth(self):
        return 'Some numbers are even'

In [11]:

class D(B,C):
    def truth(self,num):
        if num%2 == 0:
            return A.truth(self)
        else:
            return super().truth()
            
d = D()
d.truth(6)

