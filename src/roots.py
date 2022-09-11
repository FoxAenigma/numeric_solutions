import numpy as np
import src.utils as ut

def interval_method(f, inter, tol=0.001, max_loop=1000, history = False, summary=False):
	a = inter[0]
	b = inter[1]
	i = 1
	err = [100]
	m = []
	while (err[-1] > tol) and (i < max_loop):
		polarity = f(a)*f(b)
		m.append((a+b)/2)
		if polarity < 0:
			b = m[-1]
		elif polarity > 0:
			a = m[-1]
		else:
			if f(a) == 0: m.append(a)
			elif f(b) == 0: m.append(b)
			break
		err.append(abs((b-a)/2))
		i += 1
	err.pop(0)

	if summary:
		print(
			f"""
			type: root
			method: interval
			iterations: {i+1}
			error vector: {err}
			median vector: {m}
			last error: {err[-1]}
			root: {m[-1]}
			"""
		)

	if history:
		return m[-1], err[-1], [m, err]
	else:
		return m[-1], err[-1]

def fixed_point_method(f, g, x0, tol=0.001, max_loop=1000, history = False, summary=False):
	# g -> redefined f(x)=0 like x=g(x)
	# err -> |x(n)-x(n-1)|
	r = np.array([g(x0)])
	err = np.array([100])

	i=1
	while err[-1] > tol and i < max_loop:
		r_plus = g(r[-1])
		err_plus = np.abs(r[-1]-r_plus)
		i += 1

		#Append
		r = np.append(r, r_plus)
		err = np.append(err, err_plus)
	
	err = err[1:]

	summary = {
		"type": "root",
		"method": "fixed point",
		"iter": i,
		"err": err_plus,
		"root": r_plus,
	}

	if summary: ut.print_summary(summary)

	if history:
		return r_plus, err_plus, [r, err]
	else:
		return r_plus, err_plus



	return