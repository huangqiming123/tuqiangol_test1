from sympy import *

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

print(solve([2 * x - y, 3 * x + y - 7, x + z - 5], [x, y, z]))
