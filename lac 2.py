from sympy import *
from sympy.abc import x,y
int=integrate(x*y,(x,0,x),(y,0,y))
print("Double Integral of given function is",int)
