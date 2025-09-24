#code for hierarchical inheritance concept
class A:pass
class B(A): pass
class C(B): pass
print(C.mro())

class D(A): pass
class E(A): pass
class F(B): pass
print(F.mro())

#TODO  : show code for accesss to parent A only ..or homework

