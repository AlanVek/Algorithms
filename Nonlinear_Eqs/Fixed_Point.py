import numpy as np

# f recibe un array y devuelve un array del mismo largo (largo = largo de x)
# x debe ser un array
def fixed_point(f, x, tol, maxiter, table = False):
    xk = [np.asarray(x)]
    for k in range(maxiter):
        xk = np.append(xk, np.asarray(f(xk[-1])).reshape(1, -1), axis = 0)
        if np.linalg.norm(xk[-1] - xk[-2]) <= tol: break

    return xk if table else xk[-1]

if __name__ == '__main__':
    f = lambda x: [2 * x[0] - 3]# - x[1], x[0] + 2 * x[1]]
    x_0 = [2.9]
    tol = 1e-3
    maxiter = 100

    print(fixed_point(f, x_0, tol, maxiter, table = True))
