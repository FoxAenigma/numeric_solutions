#from num_sol.roots import interval_method
#from num_sol.roots import fixed_point_method
#from num_sol.utils import plot_function, Buffer
from num_sol.roots import interval_method, secant_method
import numpy as np

def f1(x): return -1.04*np.log(x)-1.26*np.cos(x)+0.0307*np.exp(x)

def g1(x): return np.log((1.04*np.log(x)+1.26*np.cos(x))/(0.0307))-x


interval_method(f1, interval=[0, 1], history=True)
secant_method(f1, points=[0, 1], history = True)

#b = Buffer("tiempo", "distancia", "angulo")
#b.push(tiempo=0, distancia=0, angulo=10)
#b.push(tiempo=1, distancia=2, angulo=20)
#b.print_register()
#b.plot_register(refer="tiempo", variables=["distancia", "angulo"])



#plot_function(f1, interval=[0, 2])
#fixed_point_method(f1, g1, x0=0.1, summary=True)


#r1, err1 = interval_method(f1, [1.4, 4], tol=1e-5, history=False, summary=True)

#r1, err1, h = inter_value(f1, [2, 3.5], tol=1e-5, history=True)
#print(r1)
#print(err1)
#plot_history(h)
