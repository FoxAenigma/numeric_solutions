import numpy as np
from sympy import poly, Symbol
from sympy.abc import x

class TaylorExpansion:
	func: 
	expandForm: sympy.Poly = None
	
	def __init__(self, f):
		self.function = self.symFunc(f)
		return

	def symFunc(self, f):
		return f(Symbol('x'))

	def expand(self, x0, n):
		pass


if __name__=="__main__":
	expansion1 = TaylorExpansion()

