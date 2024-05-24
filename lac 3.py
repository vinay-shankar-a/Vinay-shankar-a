from sympy import *
from sympy.abc import x,y
Int=integrate(1,(y,(x**2)/(4),2*(x)**0.5),(x,0,4))
print("Double integral of given function: ",Int)
