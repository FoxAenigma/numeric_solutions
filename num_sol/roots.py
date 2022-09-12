import num_sol.utils as ut
from num_sol.utils import Buffer


def interval_method(f, interval, tol = 0.001, max_loop= 1000, plotting = False, history = False):
    
    def middle(a, b):
        return (a+b)/2

    def error(a, b):
        return (b-a)/2

    interval_buffer = Buffer()
    interval_buffer.create("i", "a", "b", "xi", "err")

    a = interval[0]
    b = interval[1]
    i = 0
    m = middle(a, b)
    err = error(a, b)
    interval_buffer.push(i=i, a=a, b=b, xi=m, err=err)

    while err > tol and i < max_loop:
        polarity = f(a)*f(m)
        if polarity > 0:
            a = m
        if polarity < 0:
            b = m
        if polarity == 0:
            break
        err = error(a, b)
        i += 1
        m = middle(a, b)
        interval_buffer.push(i=i, a=a, b=b, xi=m, err=err)

    if plotting:
        ut.plot_function(f, interval)
    if history:
        interval_buffer.print_register()
        print(f"root = {m}")
        interval_buffer.plot_register(refer="i", variables=["xi", "err"])
    return m

def newton_rapshon_method(f):
    return

def secant_method(f, points, tol = 0.001, max_loop = 1000, plotting = False, history = False):
    
    def pPlus(f, p0, p1):
        return p1-(f(p1)*(p1-p0))/(f(p1)-f(p0))
    
    secant_buffer = Buffer()
    secant_buffer.create("i", "xn", "xnPlus", "err")
    i = 0
    xn = points[0]
    xnPlus = points[1]
    err = abs(f(xnPlus))
    secant_buffer.push(i=i, xn=xn, xnPlus=xnPlus, err=err)

    while err > tol and i < max_loop:
        current = xn
        xn = xnPlus
        xnPlus = pPlus(f, current, xnPlus)
        err = abs(f(xnPlus))
        i += 1
        secant_buffer.push(i=i, xn=xn, xnPlus=xnPlus, err=err)
    if plotting:
        ut.plot_function(f, points)
    if history:
        secant_buffer.print_register()
        print(f"root = {xnPlus}")
        secant_buffer.plot_register(refer="i", variables=["xnPlus", "err"])
    return xnPlus

def false_position_method(f, interval, tol = 0.001, max_loop = 1000, plotting = False, history = False):
    def pPlus(f, a, b):
        return (a*f(b)-b*f(a))/(f(b)-f(a))
    
    def error(xi, xiMinus):
        return abs(xi-xiMinus)

    false_buffer = Buffer()
    false_buffer.create("i", "a", "b", "xi", "err")
    i = 0
    a = interval[0]
    b = interval[1]
    xi = pPlus(f, a, b)
    err = error(xi, a)
    false_buffer.push(i=i, a=a, b=b, xi=xi, err=err)
    
    err = tol+1
    while err > tol and i < max_loop:
        last = xi
        polarity = f(a)*f(xi)
        if polarity > 0:
            a = xi
        if polarity < 0:
            b = xi
        if polarity == 0:
            break
        i += 1
        xi = pPlus(f, a, b)
        err = error(xi, last)
        false_buffer.push(i=i, a=a, b=b, xi=xi, err=err)
    
    if plotting:
        ut.plot_function(f, interval)
    if history:
        false_buffer.print_register()
        print(f"root = {xi}")
        false_buffer.plot_register(refer="i", variables=["xi", "err"])
    return xi


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
