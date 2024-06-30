# inheritance.py
class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()

class C(B):
    def spam(self):
        print('C.spam')
        super().spam()


class Base:
    def spam(self):
        print('Base.spam')

class X(Base):
    def spam(self):
        print('X.spam')
        super().spam()

class Y(Base):
    def spam(self):
        print('Y.spam')
        super().spam()

class Z(Base):
    def spam(self):
        print('Z.spam')
        super().spam()

class M(X,Y,Z):
    pass

class N(Z,Y,X):
    pass
