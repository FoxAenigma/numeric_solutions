import matplotlib.pyplot as plt
import numpy as np

def plot_history(h):
	m = h[0]
	err = h[1]
	
	plt.stairs(m, color="blue", baseline=None)
	plt.stairs(err, color="red", baseline=None)
	plt.show()
	return

def plot_function(f, interval=[-10, 10], n=1000):
	x = np.linspace(interval[0], interval[1], n)
	y = np.array(list(map(f, x)))
	plt.plot(x, y)
	plt.grid()
	plt.show()
	return

def print_summary(summary):
	msg = f"""
	type: {summary["type"]}
	method: {summary["method"]}
	iterations: {summary["iter"]}
	error: {summary["err"]}
	root: {summary["root"]}
	"""
	print(msg)
	return

