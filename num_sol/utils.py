import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sym

class Buffer:
    
    def __init__(self):
        self.register = {}
        return

    def create(self, *memory: str):
        for category in memory:
            self.register[category] = []
        return

    def push(self, **category):
        for key, value in category.items():
            self.register[key].append(value)
        return

    def print_register(self):
        table = pd.DataFrame(self.register)
        print(table.to_string(index = False))
        return

    def plot_register(self, refer, variables: list, title=None):
        fig, axs = plt.subplots(len(variables), 1) 
        axs[0].set_title(title)
        k = 0
        for var in variables:
            axs[k].stairs(self.register[var], baseline = None)
            axs[k].grid()
            axs[k].legend(var, loc = "upper right")
            k += 1
        return

    def get_register(self):
        return self.register
    

#Functions
def plot_function(f, interval, n=1000):
	x = np.linspace(interval[0], interval[1], n)
	y = np.array(list(map(f, x)))
	plt.plot(x, y)
	plt.grid()
	plt.show()
	return

def derivate(f):
    x = sym.Symbol('x')
    func = f(x)
    prim = sym.diff(func)
    return func, prim


