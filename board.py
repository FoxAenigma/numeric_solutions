from src.roots import interval_method
from src.roots import fixed_point_method
from src.utils import plot_function, plot_history
import numpy as np

def f1(x): return -1.04*np.log(x)-1.26*np.cos(x)+0.0307*np.exp(x)

def g1(x): return np.log((1.04*np.log(x)+1.26*np.cos(x))/(0.0307))-x

plot_function(f1, interval=[0, 2])
fixed_point_method(f1, g1, x0=0.1, summary=True)


#r1, err1 = interval_method(f1, [1.4, 4], tol=1e-5, history=False, summary=True)

#r1, err1, h = inter_value(f1, [2, 3.5], tol=1e-5, history=True)
#print(r1)
#print(err1)
#plot_history(h)
