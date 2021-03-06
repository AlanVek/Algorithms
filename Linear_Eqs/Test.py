from Gauss_Seidel import gauss_seidel
from Jacobi import jacobi
from SOR import sor
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # coef = np.array([[6, 2, 1],
    #                  [-1, 8, 2],
    #                  [1, -1, 6]])
    coef = np.random.randint(-50, 50, (20, 20))
    coef = coef.T.dot(coef)
    y = np.random.randint(-5, 5, coef.shape[0])

    tol, maxiter = 1e-6, 2000
    w = 1.2

    ok = np.linalg.solve(coef, y)

    gs = gauss_seidel(coef, y, maxiter = maxiter, tol = tol, table = True)
    # jc = jacobi(coef, y, maxiter = maxiter, tol = tol, table = True)
    sr = sor(coef, y, w, maxiter = maxiter, tol = tol, table = True)

    print('Solution     :', ok)

    print('Gauss-Seidel :', gs[0], gs[1].shape[0])
    # print('Jacobi       :', jc[0], jc[1].shape[0])
    print(f'SOR (w = {w}):', sr[0], sr[1].shape[0])

    plt.plot(ok, label = 'Real', linewidth = 0, marker = 'o')
    plt.plot(gs[0], label = 'Gauss-Seidel', linewidth = 0, marker = 's')
    plt.plot(sr[0], label = fr'SOR $\omega = {w}$', linewidth = 0, marker = 'x')
    plt.minorticks_on()
    plt.grid(which = 'both')
    plt.legend()
    plt.tight_layout()
    plt.show()

    # for j in range(coef.shape[1]):
    #     fig, ax = plt.subplots(1)
    #     ax.hlines(ok[j],
    #               0, max(gs[1].shape[0], jc[1].shape[0], sr[1].shape[0]),
    #               linestyle = '--', color = 'red', label = 'Real'
    #     )
    #
    #     ax.plot(gs[1][1:, j], label = 'Gauss-Seidel', color = 'blue')
    #     ax.plot(jc[1][1:, j], label = 'Jacobi', color = 'orange')
    #     ax.plot(sr[1][1:, j], label = fr'SOR ($\omega$ = {w})', color = 'green')
    #     ax.grid()
    #     ax.legend()
    #     ax.set_title(fr'Evolución de $x_{j}$')
    #     fig.tight_layout()
    #
    # plt.show()