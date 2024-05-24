from sympy import *
from sympy.abc import x,y
int=integrate(x*y,(x,0,1),(y,0,1))
print("Double Integral of given function is",int)
