import numpy as np

def bisec(f, a : float, b : float, tol : float = 1e-15, maxiter : int = 100, table = False):

    """ Solves f(x) = 0 """

    fa, fb = f(a), f(b)
    if not fa: return np.array([a]) if table else a
    if not fb: return np.array([b]) if table else b
    if np.sign(fa) == np.sign(fb) or maxiter <= 0: return np.array([None]) if table else None

    c = []
    for k in range(maxiter):
        c = np.append(c, (a + b) / 2)
        fc = f(c[-1])
        if not fc: break

        if np.sign(fa) != np.sign(fc): b, fb = c[-1], fc
        else: a, fa = c[-1], fc

        if abs(a - b) <= 2 * tol: break

    return c if table else c[-1]
