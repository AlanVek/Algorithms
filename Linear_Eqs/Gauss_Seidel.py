import numpy as np

def gauss_seidel(
        coef: np.array,
        y: np.array,
        tol : [int, float],
        maxiter : [int],
        x: np.array = None,
        table = False):

    h, w = coef.shape

    if x is None: x_k = np.zeros(h)
    else: x_k = x.astype(float)

    if table: iters = np.zeros((0, x_k.size))

    for k in range(maxiter):
        if table: iters = np.append(iters, [x_k], axis = 0)

        x_temp = x_k.copy()

        for i in range(h):
            sum_ = np.dot(coef[i], x_k) - coef[i, i] * x_k[i]
            x_k[i] = (y[i] - sum_) / coef[i, i]

        if np.all(np.abs(x_k - x_temp) <= tol): break

    return (x_k, iters) if table else x_k


if __name__ == '__main__':
    coef = np.array([[6, 2, 1],
                     [-1, 8, 2],
                     [1, -1, 6]])

    y = np.array([22, 30, 23])
    print('Solution    :', np.linalg.solve(coef, y))

    print('Gauss-Seidel:', gauss_seidel(coef, y, 1e-9, 100))
